
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value|[0],InstanceType,State.Name,PrivateIpAddress,PublicIpAddress]' --output text

aws ec2 create-security-group --group-name websvc --description "My security group" --vpc-id vpc-83c015e8

aws ec2 describe-security-groups \
    --filters Name=vpc-id,Values=vpcID,Name=group-name,Values=default \
    --query "SecurityGroups[*].{GroupName:GroupName,GroupId:GroupId}"

# ip_address=$(aws ec2 describe-instances --query "Reservations[*].Instances[*].PublicIpAddress" --output=text)
# echo "System Ip :" $ip_address

# echo ssh -i "Python_websvc.pem" ubuntu@$ip_address
# ssh -i "Python_websvc.pem" ubuntu@$ip_address


# aws ec2 stop-instances --instance-ids i-b78a096f
# aws ec2 start-instances --instance-ids i-b78a096f
# aws ec2 terminate-instances --instance-ids [YOUR INSTANCE ID]