#Generate Key Pair
aws ec2 --profile shibutrial create-key-pair --key-name MyKeyPair10 --query 'KeyMaterial' --output text > ~/MyKeyPair10.pem
echo Key Pair saved to your home directory
