import boto3
import logging
from ec2_instance import awsec2 



ec2_cli = boto3.client('ec2')
ec2_res = boto3.resource('ec2')

def main_create_instance():
    # Enter the below values 
    image_id = str(input('Enter the EC2 Image Id :'))
    instance_type = str(input('Enter the EC2 Instance Type :'))
    keypair_name = str(input('Enter the EC2 Keypair :'))

    # image_id = 'ami-03ffa9b61e8d2cfda'
    # instance_type = 't2.micro'
    # keypair_name = 'Python_websvc'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Provision and launch the EC2 instance
    instance_info = awsec2.create_ec2_instance(image_id, instance_type, keypair_name)
    print(instance_info)
    if instance_info is not None:
        logging.info(f' Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info(f' VPC ID: {instance_info["VpcId"]}')
        logging.info(f' Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info(f' Current State: {instance_info["State"]["Name"]}')



def main_terminate_instance():
    # Assign these values before running the program
    # ec2_instance_ids = instance_id
    awsec2.get_public_ip()
    instance_id = str(input('Enter the EC2 Instance id :'))
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
   
    # Terminate the EC2 instance(s)
    states = awsec2.terminate_instances(instance_id)
    if states is not None:
        logging.debug('Terminating the following EC2 instances')
        for state in states:
            logging.debug(f' ID: {state["InstanceId"]}')
            logging.debug(f' Current state: Code {state["CurrentState"]["Code"]}, '
                          f'{state["CurrentState"]["Name"]}')
            logging.debug(f' Previous state: Code {state["PreviousState"]["Code"]}, '
                          f'{state["PreviousState"]["Name"]}')


def main_public_ip():
    awsec2.get_public_ip()


def main():
    print("1. Create Instance")
    print("2. Delete Instance")
    print("3. List Instances & Public IP's")
    print("4. List Instance / Public IP")
    print("5. Start Instance")
    print("6. Stop Instance")
    print("7. Reboot Instance")
    Choice = str(input('Choice :'))
    

    if Choice == "1":
        main_create_instance()
    elif Choice == "2":
        main_terminate_instance()
    elif Choice == "3":
        awsec2.get_public_ip()
    elif Choice == "4":
        awsec2.get_public_ip()
        instance_id = str(input('Enter the EC2 Instance id :'))
        awsec2.get_inst_public_ip(instance_id) #-- Not Working Need To Check
    elif Choice == "5":
        awsec2.get_public_ip()
        instance_id = str(input('Enter the EC2 Instance id :'))
        action      = "start"
        awsec2.ec2_instance_start_stop(action,instance_id)
    elif Choice == "6":
        awsec2.get_public_ip()
        instance_id = str(input('Enter the EC2 Instance id :'))
        action      = "stop"
        awsec2.ec2_instance_start_stop(action,instance_id)
    elif Choice == "7":
        awsec2.ec2_instance_reboot(instance_id)
    elif Choice == " ":
        print("Invalid Choice")
        

if __name__ == '__main__':
    main()
