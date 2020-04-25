import subprocess
import sys
import time
import os
from tempfile import mkstemp
from shutil import move
from ec2_instance import ec2_parm
from command import cmd_exec


#=======================================
#	Functions
#=======================================
def usage():
	global version
	print("")
	print("python ec2_ops.py steps|create|start|stop|destroy [--profile aws_profile_name]")
	print("version: {}".format(ec2_parm.version))
	print("")
	print("  --profile = Specify the aws profile to use for Instance")
	print("")
	print("   EC2 Instance Steps:")
	print("   0. Create EC2 Instance")
	print("   1. List Instances ")
	print("   3. Start Instance")
	print("   4. Stop Instance")
	print("   5. Reboot Instance")
	print("")
	print("  Delete Steps:")
	print("   0. Terminate EC2 Instance")
	print("")
	sys.exit(0)

# Describe one or more EC2 instances
def ec2_instance_list():
    cmd_exec.execute_command("aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value|[0],InstanceType,State.Name,PrivateIpAddress,PublicIpAddress]' --output text", False)


# Provision and launch an EC2 instance
# def create_ec2_instance(image_id, instance_type, keypair_name):

#Get the public ip address
# def get_public_ip():

# Start and Stop Instances
# def ec2_instance_start_stop(action,instance_id):

# Request a reboot of one or more instances using
# def ec2_instance_reboot(instance_id):

#Terminate one or more Amazon EC2 instances
# def terminate_instances(instance_id):
