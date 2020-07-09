"""
Name: transfer.py
Created by: Masato Shima
Created on: 2020/07/09
Description:
"""

# **************************************************
# ----- Import Library
# **************************************************
import os
import argparse
import logging

import pendulum


# **************************************************
# ----- Constants & Variables
# **************************************************
# このアプリケーションの戻り値
EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAILURE = 1

CURRENT_TIME = pendulum.now("Asia/Tokyo")


# **************************************************
# ----- Set logger
# **************************************************
logging.basicConfig(
	format="%(asctime)s:[%(name)s] %(message)s",
	level=logging.INFO
)


# **************************************************
# ----- Arg parse
# **************************************************
# Create parser
parser = argparse.ArgumentParser(
	prog="transfer.py",
	usage="Run Script with appropriate arguments (-h, --help) .",
	description="Transport the file.",
	epilog="End",
	add_help=True
)

# Set parameter
parser.add_argument(
	"-p",
	"--path",
	action="store",
	required=True,
	help=""
)

parser.add_argument(
	"-f",
	"--file",
	action="store",
	required=True,
	help=""
)

parser.add_argument(
	"-e",
	"--event",
	action="store",
	required=True,
	help=""
)

args = parser.parse_args()


# **************************************************
# ----- Function
# **************************************************
def main() -> None:
	logging.info(f"Path: {args.path}")
	logging.info(f"File: {args.file}")
	logging.info(f"Event: {args.event}")

	timestamp = CURRENT_TIME.strftime('%Y%m%d%H%M%S')

	with open(f"/opt/event_{timestamp}.txt", "w", encoding="utf-8") as file:
		file.write(f"Path: {args.path}")
		file.write(f"File: {args.file}")
		file.write(f"Event: {args.event}")

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
