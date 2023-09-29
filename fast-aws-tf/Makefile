all:

plan:
	terraform validate
	terraform plan -out terraform.tfplan

format:
	terraform fmt

aws-ping:
	aws sts get-caller-identity

destroy:
	terraform destroy