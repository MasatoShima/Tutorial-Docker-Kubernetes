# """
# Name: Dockerfile
# Description: sample DockerFile from chapter 10.6
# Created by: Masato Shima
# Created on: 2020/01/20
# """

FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y iputils-ping dnsutils curl apt-transport-https

# install kubectl
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN touch /etc/apt/sources.list.d/kubernetes.list
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubectl

# install pyhon, python-packages
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get install -y python3.6 python3-pip
RUN pip3 install pika kubernetes

# End
