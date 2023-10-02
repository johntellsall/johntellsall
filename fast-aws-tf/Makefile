all:

plan:
	terraform validate
	terraform plan -out terraform.tfplan

apply:
	terraform apply terraform.tfplan

# XX "plan" auto-validates // terraform validate

plan-apply:  # plan and apply in one step
	terraform apply -auto-approve -refresh=true

format:
	terraform fmt

aws-ping:
	aws sts get-caller-identity

destroy:
	terraform destroy

devloop: aws-ping
	git ls-files | entr -c make plan

devloop-auto-apply: aws-ping
	git ls-files | entr -c make plan-apply

check:
	./check.sh