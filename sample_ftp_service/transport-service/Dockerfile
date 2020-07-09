# """
# Name: Dockerfile
# Description: Dockerfile
# Created by: Masato Shima
# Created on: 2020/07/08
# """

FROM centos:centos7.7.1908

# Install
WORKDIR /

COPY packages/incron-0.5.12-11.el7.x86_64.rpm /opt/

RUN yum -y install python3 python3-pip \
 && yum -y --nogpgcheck localinstall /opt/incron-0.5.12-11.el7.x86_64.rpm

RUN pip3 install pendulum

# Copy resources
COPY config/incron_table /opt/
COPY transfer.py /opt/

# ENTRYPOINT
ENTRYPOINT /usr/sbin/incrond start | incrontab /opt/incron_table |tail -f /dev/null

# End
