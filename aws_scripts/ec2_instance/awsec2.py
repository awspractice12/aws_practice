import sys
import boto3
import logging
from botocore.exceptions import ClientError

ec2_cli = boto3.client('ec2')
ec2_res = boto3.resource('ec2')

# Describe one or more EC2 instances
def ec2_instance_list():
    response = ec2_cli.describe_instances()
    print(response)

# ec2_instance_list()    

#Create keypair for ec2 instance
def ec2_cr8_keypair(keypair_name):
    try:
        response = ec2_cli.create_key_pair(KeyName=keypair_name)
    except ClientError as e:
        logging.error(e)
        return None
    print (response)

# ec2_cr8_keypair('arun')

#Delete keypair for ec2 instance
def ec2_dl8_keypair(keypair_name):
    try:
        response = ec2_cli.delete_key_pair(KeyName=keypair_name)
    except ClientError as e:
        logging.error(e)
        return None
    print (response)

# ec2_dl8_keypair('arun')


#Create Security Group
def ec2_cr8_security_group(security_group_name,description):
    response = ec2_cli.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
    
    try:
        response = ec2_cli.create_security_group(GroupName=security_group_name,
                                             Description=description,
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
    
        data = ec2_cli.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(e)
 
# ec2_cr8_security_group("arun","test group")

#Delete Security Group
def ec2_dl8_security_group(security_group_id):
    response = ec2_cli.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
    try:
        response = ec2_cli.delete_security_group(GroupId=security_group_id)
        print('Security Group Deleted %s in vpc %s.' % (security_group_id, vpc_id))
    except ClientError as e:
        print(e)
 
# ec2_dl8_security_group("sg-07979a7e69f712249")


# Provision and launch an EC2 instance
def create_ec2_instance(image_id, instance_type, keypair_name):
    try:
        response = ec2_cli.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]

#Get the public ip address
def get_public_ip():
    try:
        paginator = ec2_cli.get_paginator('describe_instances')
        for response in paginator.paginate():
            instance_id = response['Reservations'][1]['Instances'][0]['InstanceId']
            public_ip   = response['Reservations'][1]['Instances'][0]['PublicIpAddress']
            print("Instance ID :  {} Public IP : {}".format(
                    instance_id,
                    public_ip))
            return public_ip
    except Exception as e:
        print(e)

# get_public_ip()

#Get the specific  instance public ip address
def get_inst_public_ip(instance_id):
    try:
        [instance_id] = instance_id
        public_ip  = ec2_cli.describe_instances(InstanceIds=[{instance_id}])['Reservations'][0]['Instances'][0]['PublicDnsName']
        return public_ip
    except Exception as e:
        print(e)

# get_inst_public_ip('i-0f3120acec1ed16bd')

# get_public_ip(instance_id)
#Terminate one or more Amazon EC2 instances
def terminate_instances(instance_id):
    try:
        states = ec2_cli.terminate_instances(InstanceIds=[instance_id])
    except ClientError as e:
        logging.error(e)
        return None
    return states['TerminatingInstances']

# terminate_instances(['i-05c6b091fa99ed3c6'])

# Start and Stop Instances
def ec2_instance_start_stop(action,instance_id):
    if action == 'start':
        # Do a dryrun first to verify permissions
        try:
            ec2_cli.start_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise
    
        # Dry run succeeded, run start_instances without dryrun
        try:
            response = ec2_cli.start_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)
    else:
        # Do a dryrun first to verify permissions
        try:
            ec2_cli.stop_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise
    
        # Dry run succeeded, call stop_instances without dryrun
        try:
            response = ec2_cli.stop_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
        except ClientError as e:
            print(e)


# ec2_instance_start_stop('OFF','i-0be2fe9f8e2d73e19')

# Request a reboot of one or more instances using
def ec2_instance_reboot(instance_id):
    try:
        ec2_cli.reboot_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print("You don't have permission to reboot instances.")
            raise
    
    try:
        response = ec2_cli.reboot_instances(InstanceIds=[instance_id], DryRun=False)
        print('Success', response)
    except ClientError as e:
        print('Error', e)