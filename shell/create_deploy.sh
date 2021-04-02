cd myvenv/lib/python3.*/site-packages
zip -r ../../../../my-deployment-package.zip .
cd ../../../../
zip -g my-deployment-package.zip *.py