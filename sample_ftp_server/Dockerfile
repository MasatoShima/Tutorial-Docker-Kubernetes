# """
# Name: Dockerfile
# Description:
# Created by: Masato Shima
# Created on: 2020/03/18
# """

FROM fauria/vsftpd:latest

# Create user for ftp
RUN useradd guest \
 && echo guest:guest | chpasswd \
 && mkdir /home/vsftpd/guest/ \
 && chown guest:guest /home/vsftpd/guest/

# Copy config file
ADD /config/ /etc/vsftpd/

# Restart vsftpd
# RUN systemctl restart vsftpd

# ENTRYPOINT
ENTRYPOINT ["tail", "-f", "/dev/null"]

# End
