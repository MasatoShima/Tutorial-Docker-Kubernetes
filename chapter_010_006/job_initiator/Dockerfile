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
# RUN apt-get install -y python3 python3-pip
# RUN pip3 install pika kubernetes

RUN apt install -y build-essential
RUN apt install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN apt install -y wget

RUN wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz
RUN tar -xvf Python-3.6.7.tgz
RUN cd ./Python-3.6.7/

RUN ./configure --enable-shared --enable-optimizations
RUN sudo make altinstall

RUN cd ./../
RUN rm -rf Python-3.6.7/

RUN apt-get install -y python3-pip
RUN pip3 install pika kubernetes

# End
