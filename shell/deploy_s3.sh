zip -g my-deployment-package.zip *.py
aws s3api put-object --bucket tutorial-websocket --key my-deployment-package.zip --body my-deployment-package.zip