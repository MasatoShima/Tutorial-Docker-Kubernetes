# """
# Name: Dockerfile
# Description: Sample Application
# Created by: Masato Shima
# Created on: 2019/09/18
# """

FROM python:3

WORKDIR /usr/src/app

# 必要なファイルを COPY
COPY app.py ./

# 必要なライブラリをインストール
RUN pip install responder

CMD ["python", "./app.py"]

# End
