#Generate Key Pair
aws ec2 --profile shibutrial create-key-pair --key-name MyKeyPair2 --query 'KeyMaterial' --output text > MyKeyPair2.pem
