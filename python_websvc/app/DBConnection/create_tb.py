from __future__ import print_function
import boto3
from botocore.exceptions import ClientError
from connectionManager import connectionManager as conn
import uuid

dynamodb = conn.ddbres
# Create the DynamoDB table : t_loan
table = dynamodb.create_table(
    TableName='t_loan',
    KeySchema=[
        {
            'AttributeName': 'cust_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'loan_id',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'cust_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'loan_id',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='t_loan')


# Create the DynamoDB table : t_loan_pay
table = dynamodb.create_table(
    TableName='t_loan_pay',
    KeySchema=[
        {
            'AttributeName': 'loan_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'trans_id',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'loan_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'trans_id',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# print uuid.uuid4() # uuid4 = random UUID
# print (uuid.uuid1())

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='t_loan_pay')

# Print out some data about the table.
print(table.item_count)