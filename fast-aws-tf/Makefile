all:

lambda_hello.zip:
	zip lambda_hello.zip lambda_hello.py

invoke-lambda:
	aws lambda invoke --function-name hello \
	--payload '{}' output.json
	jq < output.json '.'

plan: lambda_hello.zip
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

devloop-plan: aws-ping
	git ls-files | entr -c make plan

devloop-auto-apply: aws-ping
	git ls-files | entr -c make plan-apply
	make invoke-lambda

devloop: devloop-plan

check:
	./check.sh