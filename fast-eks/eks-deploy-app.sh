#!/usr/local/bin/bash

# deploy sample app to EKS
# https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html

set -euo pipefail # Bash strict mode

set +e # ignore error
kubectl create namespace eks-sample-app
set -e


kubectl apply -f eks-sample-deployment.yaml
kubectl apply -f eks-sample-service.yaml
