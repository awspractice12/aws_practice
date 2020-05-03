import boto3
import subprocess
import sys

pipeline = boto3.client('codepipeline')
s3_bucket = boto3.resource('s3')

def exec_cmd(command):
    p=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    
def add(event, context):
    print ("printing from ss-poc-lambda-2")

    # command='mkdir -v /tmp/code/'
    # exec_cmd(command)


    # response = s3_bucket.Object("ss-poc-code", "account-depl.yaml").download_file(f'/tmp/code/account-depl.yaml')
    # response = s3_bucket.Object("ss-poc-code", "account-service.yaml").download_file(f'/tmp/code/account-service.yaml')

    # command='ls -l /tmp/code/'
    # exec_cmd(command)
    
    # command='kubectl --version'
    # exec_cmd(command)

    command='/opt/kubectl/kubectl --version'
    exec_cmd(command)
    # command='/opt/awscli/bin/aws s3 cp s3://ss-poc-code/code.zip /tmp/code/'
    # exec_cmd(command)



    print ("Completed Unzippping.....")

    
    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return response

