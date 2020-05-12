# Create instance
aws ec2 --profile shibutrial run-instances --image-id ami-0fc20dd1da406780b --count 1 --instance-type t3.micro --key-name MyKeyPair5 --security-groups shibu-sg --user-data file://software_install_on_startup.txt  1>/dev/null
sleep 60
./50_get_public_ipaddress.sh
scp -i  ~/MyKeyPair5.pem bash_aliases.txt ubuntu@`cat ec2-hosts`:.bash_aliases

