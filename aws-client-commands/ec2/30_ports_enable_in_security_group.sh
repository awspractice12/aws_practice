#-------------------------------------------------------------------------------------
#Use above IP in below command to get fine grained control of what access is provided
#Below command with 0.0.0.0 gives access to all IP address. BE CAREFUL !!!!

#----------------------
#For SSH access alone
aws ec2 authorize-security-group-ingress --group-name shibu-sg --protocol tcp --port 22 --cidr 0.0.0.0/0
#----------------------
#For all TCP and all ports access
aws ec2 authorize-security-group-ingress --group-name shibu-sg --ip-permissions IpProtocol=tcp,FromPort=1,ToPort=65535,IpRanges=[{CidrIp=0.0.0.0/0}]
#-------------------------------------------------------------------------------------
