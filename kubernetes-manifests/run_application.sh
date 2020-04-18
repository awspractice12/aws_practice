sudo kubectl create -f  derby-db-depl.yaml
sudo kubectl create -f  derby-db-service.yaml
echo sleeping for 60 seconds
sleep 60
sudo kubectl create -f  account-depl.yaml
sudo kubectl create -f  account-service.yaml
echo sleeping for 60 seconds
sleep 60
sudo kubectl create -f  customer-depl.yaml
sudo kubectl create -f  customer-service.yaml

