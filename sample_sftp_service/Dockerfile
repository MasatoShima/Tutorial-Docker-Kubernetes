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
COPY config/sshd_config /etc/ssh/sshd_config
RUN chmod 644 /etc/sftp/users.conf
RUN chmod 644 /etc/ssh/sshd_config

# COPY public key for sftp
COPY keys/jal-srs-sftp-guest.pem.pub /home/foo/.ssh/keys/jal-srs-sftp-guest.pem.pub
COPY keys/jal-srs-sftp-guest.pem.pub /home/bar/.ssh/keys/jal-srs-sftp-guest.pem.pub
COPY keys/jal-srs-sftp-guest.pem.pub /home/baz/.ssh/keys/jal-srs-sftp-guest.pem.pub
RUN chmod 600 /home/foo/.ssh/keys/jal-srs-sftp-guest.pem.pub
RUN chmod 600 /home/bar/.ssh/keys/jal-srs-sftp-guest.pem.pub
RUN chmod 600 /home/baz/.ssh/keys/jal-srs-sftp-guest.pem.pub

# Create data directry
RUN mkdir /home/foo/data/
RUN mkdir /home/bar/data/
RUN mkdir /home/baz/data/
RUN chmod 777 /home/foo/data/
RUN chmod 777 /home/bar/data/
RUN chmod 777 /home/baz/data/

EXPOSE 22

ENTRYPOINT /entrypoint

# End
