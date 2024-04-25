#!/bin/bash

echo "Please wait a moment while CFN-guard is installed"
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/aws-cloudformation/cloudformation-guard/main/install-guard.sh | sh

echo ""
echo "CFN-Guard is installed!"

#cfn-guard --version

