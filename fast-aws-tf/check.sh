#!/usr/bin/env bash

# Check all resources to speed up development

set -euo pipefail # Bash strict mode

set +x # trace

aws ssm get-parameters-by-path --path / --recursive
# aws ssm get-parameter --name /

