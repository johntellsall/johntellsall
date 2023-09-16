# Fast Feedback for DevOps and EKS

## Goal

TBD

## Setup

- manual EKS
- local: kubectl create configmap

NOTE:

    kubectl config set-context --current --namespace=eks-sample-app

## LATER

    CloudWatch logging will not be enabled for cluster "jta-20230915" in "us-west-2"
    2023-09-15 09:51:38 [ℹ]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-west-2 --cluster=jta-20230915'

## INFO


    2023-09-15 09:51:38 [ℹ]  subnets for us-west-2d - public:192.168.0.0/19 private:192.168.96.0/19
    2023-09-15 09:51:38 [ℹ]  subnets for us-west-2c - public:192.168.32.0/19 private:192.168.128.0/19
    2023-09-15 09:51:38 [ℹ]  subnets for us-west-2b - public:192.168.64.0/19 private:192.168.160.0/19
    2023-09-15 09:51:38 [ℹ]  using Kubernetes version 1.25