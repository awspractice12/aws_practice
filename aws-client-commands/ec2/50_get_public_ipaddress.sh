aws ec2 --profile shibutrial describe-instances --filters  "Name=instance-state-name,Values=pending,running,stopped,stopping" --query "Reservations[].Instances[].PublicIpAddress" --output text | tee ec2-hosts
cat ec2-hosts
