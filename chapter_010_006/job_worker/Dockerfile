# """
# Name: Dockerfile
# Description: sample DockerFile from chapter 10.6
# Created by: Masato Shima
# Created on: 2020/01/19
# """

FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y curl ca-certificates amqp-tools python python-pip

RUN pip install numpy

COPY ./prime_number.py ./.

CMD /usr/bin/amqp-tools --url=$BROKER_URL -q $QUOTE -c 1 /prime_number.py

# End
