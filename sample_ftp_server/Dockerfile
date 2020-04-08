# """
# Name: Dockerfile
# Description: Dockerfile
# Created by: Masato Shima
# Created on: 2020/03/18
# """

FROM centos:centos7.7.1908

# Install vsftpd
RUN yum install -y vsftpd

# Create user for ftp
COPY config/users/users.txt /opt/
RUN newusers /opt/users.txt

# Copy config file
ADD config/vsftpd/ /etc/vsftpd/

# Copy shell
COPY run.sh /opt/
RUN chmod 775 /opt/run.sh

EXPOSE 20:21
EXPOSE 21100:21101

# ENTRYPOINT
ENTRYPOINT ["/opt/run.sh"]

# End
