#Generate Key Pair
aws ec2 --profile shibutrial create-key-pair --key-name MyKeyPair5 --query 'KeyMaterial' --output text > ~/MyKeyPair5.pem
echo Key Pair saved to your home directory
