# """
# Name: Dockerfile
# Description: Sample Application
# Created by: Masato Shima
# Created on: 2019/09/18
# """

FROM python:3

WORKDIR /usr/src/app

COPY app.py ./

RUN pip install responder

CMD ["python", "./app.py"]

# End
