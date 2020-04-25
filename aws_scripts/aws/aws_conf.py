import subprocess
import sys
import time
import os
from tempfile import mkstemp
from shutil import move
from aws import aws_parm 
from command import cmd_exec


#=======================================
#	Functions
#=======================================
def usage():
	global version
	print("")
	print("python aws_ops.py [--profile aws_profile_name]")
	print("version: {}".format(version))
	print("")
	print("  --profile = Specify the aws profile to setup")
	print("")
	sys.exit(0)

#Configure AWS CLI 
def configure_awscli(profile_name):
    print(divider)
    print("Starting configuration of awsclli --> {}".format(profile_name))
    print(divider)
    
    if profile_name == " ":
        rc = cmd_exec.execute_command("aws configure set aws_access_key_id {0} && aws configure set aws_secret_access_key {1} && aws configure set region {2}".format(aws_parm.AWS_ACCESS_KEY_ID, aws_parm.AWS_SECRET_ACCESS_KEY, aws_parm.AWS_DEFAULT_REGION), False)
        cmd_exec.execute_command("aws configure list ",False)
    else:
        rc = cmd_exec.execute_command("aws configure --profile {0} set aws_access_key_id {1} && aws configure --profile {0} set aws_secret_access_key {2} && aws configure --profile {0} set region {3}".format(profile_name, aws_parm.AWS_ACCESS_KEY_ID, aws_parm.AWS_SECRET_ACCESS_KEY, aws_parm.AWS_DEFAULT_REGION), False)
        cmd_exec.execute_command("aws configure list --profile {0}".format(profile_name), False)

    print(divider)
    print("Completed configuration of awsclli --> {}".format(profile_name))
    print(divider)

# #Create keypair for ec2 instance
def ec2_cr8_keypair(keypair_name,key_filename):
    rc = cmd_exec.execute_command("aws ec2 create-key-pair --key-name {0} --query 'KeyMaterial' --output text > {1}".format(keypair_name, key_filename), False)

# #Delete keypair for ec2 instance
def ec2_dl8_keypair(keypair_name):
    rc = cmd_exec.execute_command("aws ec2 delete-key-pair --key-name {0}".format(keypair_name), False)

# #Create Security Group
# def ec2_cr8_security_group(security_group_name,description):
# aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-1a2b3c4d

# #Delete Security Group
# def ec2_dl8_security_group(security_group_id):



