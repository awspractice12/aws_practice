import boto3 
import os
from os import environ

class connectionManager:
     ddbres = boto3.resource('dynamodb')
     ddbcln = boto3.client('dynamodb')
