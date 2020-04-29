import boto3
pipeline = boto3.client('codepipeline')

def lambda_handler(event, context):
    print ("printing from ss-poc-lambda-2")

    # stuff

    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return response
