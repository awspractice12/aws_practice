#Create Security Groups
aws ec2 --profile shibutrial create-security-group --group-name shibu-sg --description "Shibu security group"

#-------------------------------------------------------------------------------------
#Incase of deleting Security group...
#aws ec2 --profile shibutrial delete-security-group --group-name shibu-sg
#-------------------------------------------------------------------------------------
#See details
#aws ec2 --profile shibutrial describe-security-groups --group-names shibu-sg
#-------------------------------------------------------------------------------------
