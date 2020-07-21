#!/bin/sh -ev
# """
# Name: deploy.sh
# Created by: Masato Shima
# Created on: 2020/04/11
# Description: Shell for deploy
# """

sam deploy \
  --stack-name Tutorial-Docker-Kubernetes \
  --template-file ./template.yaml \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

# End
