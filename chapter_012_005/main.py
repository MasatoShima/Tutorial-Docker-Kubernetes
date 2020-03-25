"""
Name: main.py
Created by: Masato Shima
Created on: 2020/03/26
Description:
	sample manifest from chapter 12.5
	状態不明の node を cluster から削除する script
"""

# **************************************************
# ----- Import Library
# **************************************************
import os
import sys
import signal
import time

from kubernetes import client, config
from kubernetes.client.rest import ApiException


# **************************************************
# ----- Function handler
# **************************************************
# 停止要求に伴う, 処理を行う
def handler(signum, frame):

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
# ----- Main
# **************************************************
if __name__ == "__main__":
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	main()


# **************************************************
# ----- End
# **************************************************
