#!/usr/bin/env bash

aws cloudformation create-stack \
--region 'us-east-1' \
--stack-name tutorial-websocket \
--template-body file://formation.yml \
--capabilities CAPABILITY_IAM \
--capabilities CAPABILITY_NAMED_IAM