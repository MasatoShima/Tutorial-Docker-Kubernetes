# """
# Name: Dockerfile
# Description:
# Created by: Masato Shima
# Created on: 2020/03/18
# """

FROM centos:centos7.7.1908

# Install vsftpd
RUN yum install -y vsftpd

# Create user for ftp
RUN mkdir -p /home/ftpusers/guest/ \
 && useradd guest --home-dir /home/ftpusers/guest/ \
 && echo guest:guest | chpasswd

# Copy config file
#ADD /config/ /etc/vsftpd/

# ENTRYPOINT
ENTRYPOINT ["tail", "-f", "/dev/null"]

# End
