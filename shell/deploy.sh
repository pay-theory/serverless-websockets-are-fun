zip -g my-deployment-package.zip *.py
aws lambda update-function-code --region us-east-1 --function-name tutorial-websocket --zip-file fileb://my-deployment-package.zip