CLUSTER_NAME := jta-20230915

all:

aws-ping: ## check AWS_PROFILE set
	aws sts get-caller-identity
	@env | grep AWS_REGION

version:
	kubectl version --client
	eksctl version

eks-update-config: aws-ping
	aws eks update-kubeconfig --name $(CLUSTER_NAME)

eks-create-cluster: aws-ping
	eksctl create cluster --name $(CLUSTER_NAME) --fargate

eks-delete-cluster: aws-ping
	eksctl delete cluster --name $(CLUSTER_NAME)

eks-list:
	eksctl get cluster

# level 0: ConfigMap

cm-apply:
	kubectl create cm test --from-literal=test=yes
cm-delete:
	kubectl delete cm test

# level 1: App with Service, pre-built image

app-deploy:
	./eks-deploy-app.sh