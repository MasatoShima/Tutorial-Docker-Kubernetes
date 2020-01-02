# """
# Name: Dockerfile
# Description: sample manifest from chapter 7.6
# Created by: Masato Shima
# Created on: 2020/01/03
# """

FROM alpine:latest

RUN apt-get update && apt-get install -y git

COPY ./contents_cloner.sh ./contents_cloner.sh

RUN chmod a+x ./contents_cloner.sh

CMD ["./contents_cloner.sh"]

# End
