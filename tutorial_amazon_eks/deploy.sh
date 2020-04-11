#!/bin/sh -ev
# """
# Name: deploy.sh
# Created by: Masato Shima
# Created on: 2020/04/11
# Description: Shell for dploy
# """

sam deploy \
  --stack-name Tutorial-Docker-Kubernetes \
  --template-file ./template.yaml \
  --profile private \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

# End
