REPOSITORY_URI=732631625641.dkr.ecr.us-east-2.amazonaws.com/ss-cloud-poc-container-repo
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REPOSITORY_URI

