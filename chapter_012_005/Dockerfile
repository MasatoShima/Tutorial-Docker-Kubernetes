# """
# Name: Dockerfile
# Description: sample DockerFile from chapter 12.5
# Created by: Masato Shima
# Created on: 2020/04/23
# """

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y iputils-ping dnsutils curl apt-transport-https gnupg gnupg1 gnupg2

# install pyhon, python-packages
RUN apt-get install -y python3 python3-pip
RUN pip3 install kubernetes

# Copy scropt
COPY main.py /main.py

WORKDIR /

CMD python /main.py

# End
