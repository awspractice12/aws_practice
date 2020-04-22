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

