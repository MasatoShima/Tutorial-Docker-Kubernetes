# """
# Name: Dockerfile
# Description: sample DockerFile from chapter 10.5
# Created by: Masato Shima
# Created on: 2020/01/15
# """

FROM python:3

COPY ./prime_number.py ./.

RUN pip install numpy

CMD ["python", "./prime_number.py"]

# End
