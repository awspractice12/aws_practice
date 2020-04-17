sudo docker build . -t account-service:1.0

sudo docker tag        account-service:1.0 local:account-service-1.0
sudo docker tag        account-service:1.0 localhost:5000/local:account-service-1.0
sudo docker tag        account-service:1.0 732631625641.dkr.ecr.us-east-2.amazonaws.com/ss-cloud-poc-container-repo:account-service-1.0

sudo docker push       localhost:5000/local:account-service-1.0
