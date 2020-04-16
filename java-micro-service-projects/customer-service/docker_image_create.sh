sudo docker build . -t customer-service:1.0

sudo docker tag        customer-service:1.0 local:customer-service-1.0
sudo docker tag        customer-service:1.0 localhost:5000/local:customer-service-1.0
sudo docker tag        customer-service:1.0 732631625641.dkr.ecr.us-east-2.amazonaws.com/ss-cloud-poc-container-repo:customer-service-1.0

sudo docker push       localhost:5000/local:customer-service-1.0
