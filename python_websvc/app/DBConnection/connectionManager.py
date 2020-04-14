import boto3 
import os
from os import environ

class connectionManager:
     ddbres = boto3.resource('dynamodb', region_name=environ.get('REGION'), endpoint_url=environ.get('END_URL'))
     ddbcln = boto3.client('dynamodb', region_name=environ.get('REGION'), endpoint_url=environ.get('END_URL'))
