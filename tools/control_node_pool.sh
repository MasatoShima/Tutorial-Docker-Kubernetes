#!/bin/sh -ev
# """
# Name: control_node_pool.sh
# Created by: Masato Shima
# Created on: 2020/03/07
# Description: Change number of GKE cluster node pools
# """

POOL_NUM="$1"

gcloud container clusters resize tutorial-docker-kubernetes \
  --node-pool default-pool \
  --num-nodes "$POOL_NUM" \
  --quiet

# End
