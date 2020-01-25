# """
# Name: Dockerfile
# Description: sample DockerFile from chapter 10.6
# Created by: Masato Shima
# Created on: 2020/01/19
# """

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y curl ca-certificates amqp-tools gnupg gnupg1 gnupg2

RUN apt-get install -y python3 python3-pip
RUN pip3 install numpy

COPY ./prime_number.py ./.

CMD /usr/bin/amqp-consume --url=$BROKER_URL -q $QUOTE -c 1 /prime_number.py

# End
