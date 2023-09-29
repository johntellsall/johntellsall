DRY := -oyaml '--dry-run=client'

all:

ping:
	kubectl version

new-configmap:
	kubectl create configmap --from-literal=beer=tasty \
		$(DRY) test-configmap
