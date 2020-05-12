# #=======================================
# #	Constants
# #=======================================
# ns=""
divider="#------------------------------------------#"
version="1.0.0"

ATTEMPTS=10
WAIT_SEC=60


#===============================
#	VPC Information
#===============================
VPC_STACK_NAME="ss-poc-stack"
VPC_TEMPLATE="https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-12-10/amazon-eks-vpc-sample.yaml"
# VPC_TEMPLATE="D:\Vagrant-Projects\data\aws_scripts\yml\amazon-eks-vpc-private-subnets.yaml"


#===============================
#	EKS Cluster
#===============================
EKS_CLUSTER_NAME="ss-poc-cluster"
# EKS_ROLE_ARN="arn:aws:iam::669678783832:role/cbd-eks-role"
EKS_ROLE_ARN="arn:aws:iam::560773393352:role/ss_poc_eks_cluster_policy"
#===============================
#	EKS Worker Nodes
#===============================
EKS_NODES_TEMPLATE="https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-12-10/amazon-eks-nodegroup.yaml"
# EKS_NODES_TEMPLATE="D:\Vagrant-Projects\data\aws_scripts\yml\amazon-eks-nodegroup.yaml"
EKS_NODES_STACK_NAME="ss-poc-nodes"
EKS_NODE_GROUP_NAME="ss-poc-eks-nodes"
EKS_NODE_AS_GROUP_MIN="1"
EKS_NODE_AS_GROUP_MAX="1"
EKS_NODE_AS_GROUP_DESIRED="1"

#Amazon instance type - Refer to Amazon Documentation for available values
EKS_NODE_INSTANCE_TYPE="t3.xlarge"

#Amazon Image Id - Refer to https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html for full list.  The region is important for AMI to use.  The below is for us-east-2
EKS_IMAGE_ID="ami-053cbe66e0033ebcf"

#The IAM Key to use
EKS_KEY_NAME="MyKeyPair5"

EKS_NODE_VOLUME_SIZE="20"

#===============================
#	Secondary User
#===============================
#AWS_SECOND_USER_ARN="arn:aws:iam::500946550028:user/shibu.narayanan"
#AWS_SECOND_USER_NAME="shibu.narayanan"
