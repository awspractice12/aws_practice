export derby_server_ip=`sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps | grep derby | cut -d ' ' -f 1)`
echo Derby Server IP address = $derby_server_ip

export account_server_ip=`sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps | grep account | cut -d ' ' -f 1)`
echo Account server address = $account_server_ip

sudo docker run -d -e ACCOUNT_SERVER_URL_BASE=http://$account_server_ip:8201 -e DERBY_DB_SERVER=$derby_server_ip -e DERBY_DB_PORT=1527 -e DERBY_DB_USERNAME=shibu -e DERBY_DB_PASSWORD=shibu  -p 8101:8101 732631625641.dkr.ecr.us-east-2.amazonaws.com/ss-cloud-poc-container-repo:customer-service-1.0

