export derby_server_ip=`sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps | grep derby_shibu | cut -d ' ' -f 1)`
echo Derby Server IP address = $derby_server_ip

sudo docker run -d -e DERBY_DB_SERVER=$derby_server_ip -e DERBY_DB_PORT=1527 -e DERBY_DB_USERNAME=shibu -e DERBY_DB_PASSWORD=shibu  -p 8201:8201 --name account_shibu localhost:5000/account-service:1.0

