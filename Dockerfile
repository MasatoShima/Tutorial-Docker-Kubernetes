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

# proxy の設定を追加
RUN export HTTP_PROXY=http://172.24.2.10:8080
RUN export HTTPS_PROXY=http://172.24.2.10:8080

# 必要なライブラリをインストール
RUN pip install responder

CMD ["python", "./app.py"]

# End
