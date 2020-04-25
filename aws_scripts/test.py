import boto3
import sys

ec2_cli = boto3.client('ec2')
ec2_res = boto3.resource('ec2')

# instance = ec2_res.Instance(['i-006454a628c4c6356'])

# print(instance)

# response = ec2_cli.describe_addresses(
# )

# print(response)

# def get_public_ip():
#     try:
#         paginator = ec2_cli.get_paginator('describe_instances')
#         for response in paginator.paginate():
#             print(response)
#             instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
#             public_ip = response['Reservations'][0]['Instances']['PublicIpAddress']
#             # print("Instance ID :  {} ".format(
#             #         instance_id
#             #         ))
#             print("Instance ID :  {} Public IP :".format(
#                     instance_id,
#                     public_ip))
#     except Exception as e:
#         print(e)

# def get_public_ip():
#     try:
#         paginator = ec2_cli.get_paginator('describe_instances')
#         for response in paginator.paginate():
#             instance_id = response['Reservations'][1]['Instances'][0]['InstanceId']
#             public_ip   = response['Reservations'][1]['Instances'][0]['PublicIpAddress']
#             print("Instance ID :  {} Public IP : {}".format(
#                     instance_id,
#                     public_ip))
#             return public_ip
#     except Exception as e:
#         print(e)
   
# get_public_ip()


# response = ec2_cli.allocate_address(
#     Domain='vpc',
# )
# print(response)

# import boto3

# def get_console_output(instance_id):
#     """
#     Using EC2 GetConsoleOutput API according
#         https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html
#     """
#     ec2 = boto3.resource('ec2')
#     ec2_instance = ec2.Instance(instance_id)
#     json_output = ec2_instance.console_output()

#     return json_output.get('Output', '')

# if len(sys.argv) == 1:
#     print("Usage: {0} <instance-id>".format(sys.argv[0]))
#     sys.exit(1)
# instance_id = sys.argv[1]
# output = get_console_output(instance_id)
# print(output)    



# from tkinter import *
# master = Tk() 
# var1 = IntVar() 
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W) 
# var2 = IntVar() 
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W) 
# mainloop() 



# from tkinter import *
# master = Tk() 
# Label(master, text='First Name').grid(row=0) 
# Label(master, text='Last Name').grid(row=1) 
# e1 = Entry(master) 
# e2 = Entry(master) 
# e1.grid(row=0, column=1) 
# e2.grid(row=1, column=1) 
# mainloop() 


import sys
from tkinter import *

myApp = Tk()
myApp.title('My App')

myApp.geometry('400x400+350+340')

label = Label(text='My Label', fg ='red', bg = 'white').grid(row=0,column=0,sticky=E)

myApp.mainloop()