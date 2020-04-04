"""
Name: main.py
Created by: Masato Shima
Created on: 2020/03/26
Description:
	sample script from chapter 12.5
	状態不明の node を cluster から削除する script
"""

# **************************************************
# ----- Import Library
# **************************************************
import os
import sys
import signal
import time
import traceback

from kubernetes import client, config
from kubernetes.client.rest import ApiException


# **************************************************
# ----- Constant & Variables
# **************************************************
# 状態が不明になった node の情報を格納
# key は node 名, value は不明状態のカウント数
unknown_node = {}


# **************************************************
# ----- Function handler
# **************************************************
# 停止要求に伴う, 処理を行う
def handler(signum, frame):
	print(
		f"Received stop request"
		f"{signum}"
		f"{frame}"
	)

	sys.exit(0)


# **************************************************
# ----- Function delete_node
# **************************************************
# 引数で渡された情報をもとに, 対象の node を削除する
def delete_node(v1, name):
	body = client.V1DeleteOptions()

	try:
		_ = v1.delete_node(name, body)
		print(f"Delete node -> {name}")
	except ApiException as error_info:
		print(f"Exception when calling CoreV1Api -> delete node {error_info}")

	return


# **************************************************
# ----- Function monitoring_node
# **************************************************
# node の監視を行う
def monitoring_node(v1):
	try:
		# node の一覧を取得
		node_list = v1.list_node(watch=False)

		# node を 1つずつ, 参照し, 状態確認を行う
		for i in node_list.items():
			node_name = i.metadata.name

			for j in i.status.conditions:
				if (j.type == "Ready") and (j.status != "True"):
					if node_name in unknown_node:
						unknown_node[node_name] += 1
					else:
						unknown_node[node_name] = 0

					print(f"Unknown node: {node_name} count: {unknown_node[node_name]}")

				# 状態不明の回数が 3回を超えた場合は, 該当する node を削除
				if unknown_node[node_name] > 3:
					del unknown_node[node_name]
					delete_node(v1, i.metadata.name)

				# node の状態が正常状態に戻った場合は, unknown_node より該当する node を削除
				if (j.type == "Ready") and (j.status == "True"):
					if node_name in unknown_node:
						del unknown_node[node_name]

	except Exception as error_info:
		print(
			f"Exception when calling CoreV1Api -> list_node\n"
			f"{error_info}"
			f"{traceback.format_exc()}"
		)

	return


# **************************************************
# ----- Main
# **************************************************
if __name__ == "__main__":
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	# シグナル処理
	signal.signal(signal.SIGTERM, handler)

	# 認証情報の取得
	config.load_incluster_config()

	# インスタンス化
	client_v1 = client.CoreV1Api()

	# 定間隔で node を監視
	while True:
		monitoring_node(client_v1)

		time.sleep(5)


# **************************************************
# ----- End
# **************************************************
