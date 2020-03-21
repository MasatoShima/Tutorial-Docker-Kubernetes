#!/bin/sh
# """
# Name: Dockerfile
# Description: Dockerfile
# Created by: Masato Shima
# Created on: 2020/03/18
# """

# Run vsftpd
/usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf

# Run tail
tail -f /dev/null

# End
