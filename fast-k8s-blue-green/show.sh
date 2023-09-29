#!/usr/bin/env bash

set -euo pipefail # Bash strict mode

BOLD_GREEN='\033[1;32m'
NORMAL='\033[0m'

echo -e "${BOLD_GREEN}Resources${NORMAL}"
kubectl get cm
kubectl get all
