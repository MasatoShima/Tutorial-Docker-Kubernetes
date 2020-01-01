"""
Name: app.py
Description: Sample Application
Created by: Masato Shima
Created on: 2020/01/01
"""

# **************************************************
# ----- Import Library
# **************************************************
import datetime
import responder


# **************************************************
# ----- Constants & Variables
# **************************************************
START_TIME = datetime.datetime.today()


# **************************************************
# ----- Process Main
# **************************************************
api = responder.API()


# **************************************************
# ----- Method root
# **************************************************
@api.route("/")
def hello_world(req, res):
	content = "Hello World !"

	res.text = content

	return


# **************************************************
# ----- Method health
# **************************************************
# Liveness Probe 用の handler
@api.route("/health")
def health(req, res):
	elapsed_time = datetime.datetime.today() - START_TIME

	# 擬似的に起動から 20秒間を起動処理中とする
	# 起動から 20秒以内は 500応答を返す
	# 起動から 20秒以降は 200応答を返す
	if elapsed_time.seconds <= 40:
		res.status_code = api.status_codes.HTTP_200
	else:
		res.status_code = api.status_codes.HTTP_500

	return


# **************************************************
# ----- Method ready
# **************************************************
# Rediness Probe 用の handler
@api.route("/ready")
def ready(req, res):
	elapsed_time = datetime.datetime.today() - START_TIME

	# 起動から 20秒以内は 500応答を返す
	# 起動から 20秒以降は 200応答を返す
	if elapsed_time.seconds <= 20:
		res.status_code = api.status_codes.HTTP_500
	else:
		res.status_code = api.status_codes.HTTP_200

	return


# **************************************************
# ----- Start
# **************************************************
api.run(address="0.0.0.0", port=8000)


# **************************************************
# ----- End
# **************************************************
