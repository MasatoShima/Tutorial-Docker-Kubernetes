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
@api.route("/health")
def health(req, res):
	elapsed_time = datetime.datetime.today() - START_TIME

	if elapsed_time.seconds <= 20:
		res.status_code = api.status_codes.HTTP_200
	else:
		res.status_code = api.status_codes.HTTP_500

	return


# **************************************************
# ----- Method ready
# **************************************************
@api.route("/ready")
def ready(req, res):
	elapsed_time = datetime.datetime.today() - START_TIME

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
