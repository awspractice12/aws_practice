echo -----------------------------------------

sudo kubectl delete deployment account-depl
sudo kubectl delete service service-account

sudo kubectl delete deployment customer-depl
sudo kubectl delete service service-customer

sudo kubectl delete deployment loan-depl
sudo kubectl delete service service-loan

sudo kubectl delete deployment derby-db-depl
sudo kubectl delete service derby-db-service

echo -----------------------------------------

sudo kubectl apply -f  derby-db-depl.yaml
sudo kubectl apply -f  derby-db-service.yaml
echo -----------------------------------------
#echo sleeping for 60 seconds
#sleep 60
sudo kubectl apply -f  account-depl.yaml
sudo kubectl apply -f  account-service.yaml
echo -----------------------------------------
#echo sleeping for 60 seconds
#sleep 60
sudo kubectl apply -f  customer-depl.yaml
sudo kubectl apply -f  customer-service.yaml
echo -----------------------------------------
#echo sleeping for 60 seconds
#sleep 60
sudo kubectl apply -f  loan-depl.yaml
sudo kubectl apply -f  loan-service.yaml
echo -----------------------------------------

