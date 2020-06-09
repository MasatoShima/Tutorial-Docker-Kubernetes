# """
# Name: Dockerfile
# Created by: Masato Shima
# Created on: 2020/06/09
# Description:
#   Dockerfile
#   SFTP 受信が可能な環境を構築する
# """

FROM atmoz/sftp

WORKDIR /

# COPY configure file
COPY config/users.conf /etc/sftp/users.conf
RUN chmod 644 /etc/sftp/users.conf

EXPOSE 22

ENTRYPOINT /entrypoint

# End
