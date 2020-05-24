from __future__ import print_function # Python 2/3 compatibility
from flask import Flask, jsonify
from DBConnection.connectionManager import connectionManager as conn
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import boto3
import json
import sys

class loan_entry:
    def loan_load(cust_id,loan_id,granted_date,principal_amount,rate_of_interest,loan_duration,monthly_payment,loan_status):
        try:
            table_name = "t_loan" 
            dynamodb = conn.ddbcln
            response = dynamodb.put_item(
                TableName=table_name,
                Item={
                    "cust_id": {"S": f"{cust_id}"},
                    "loan_id": {"S": f"{loan_id}"},
                    "granted_date": {"S": f"{granted_date}"},
                    "principal_amount": {"N": f"{principal_amount}"},
                    "rate_of_interest": {"N": f"{rate_of_interest}"},
                    "loan_duration": {"N": f"{loan_duration}"},
                    "monthly_payment": {"N": f"{monthly_payment}"},
                    "loan_status": {"S": f"{loan_status}"},
                }
            )
        except ClientError as err:
            print(err)
        else:
            return response

# class loan_update:


class loan_retrive:

    def get_all_loans():
        dynamodb = conn.ddbres
        loan_table = dynamodb.Table('t_loan')
        customer = loan_table.scan()['Items']
        return customer

    def retrievecust(cust_id):
        dynamodb = conn.ddbres
        loan_table = dynamodb.Table('t_loan')
        filtering_exp = Key('cust_id').eq(cust_id)
        customer = loan_table.scan(FilterExpression=filtering_exp)['Items']
        # customer = table.query(KeyConditionExpression=Key('cust_id').eq(cust_id))
        return customer
          
    def retrieveloan(cust_id,loan_id):
        dynamodb = conn.ddbres
        loan_table = dynamodb.Table('t_loan')
        filtering_exp = Key('cust_id').eq(cust_id)
        filtering_exp2 = Key('loan_id').eq(loan_id)
        loan_rec = loan_table.scan(FilterExpression=filtering_exp and filtering_exp2)['Items']
        # loan_rec = table.query(KeyConditionExpression=Key('cust_id').eq(cust_id) & Key('loan_id').eq(loan_id))
        return loan_rec
        

class loan_payment:
    def loan_payment(loan_id,trans_id,trans_date,installment_no,installment_amt):
        try:
            table_name = "t_loan_pay" 
            dynamodb = conn.ddbcln
            response = dynamodb.put_item(
                TableName=table_name,
                Item={
                    "loan_id": {"S": f"{loan_id}"},
                    "trans_id": {"S": f"{trans_id}"},
                    "trans_date": {"S": f"{trans_date}"},
                    "installment_no": {"N": f"{installment_no}"},
                    "installment_amt": {"N": f"{installment_amt}"},
                }
            )
        except ClientError as err:
            print(err)
        else:
            return response


# class payment_update:


class payment_retrive:

    def get_all_pay():
        dynamodb = conn.ddbres
        pay_table = dynamodb.Table('t_loan_pay')
        payments = pay_table.scan()['Items']
        return payments

    def retrieve_cust_pay(loan_id):
        dynamodb = conn.ddbres
        pay_table = dynamodb.Table('t_loan_pay')
        filtering_exp = Key('loan_id').eq(loan_id)
        pay_det = pay_table.scan(FilterExpression=filtering_exp)['Items']
    	# pay_det = table.query(KeyConditionExpression=Key('loan_id').eq(loan_id))
        return pay_det

    def retrieve_loan_pay(loan_id,trans_id):
        dynamodb = conn.ddbres
        pay_table = dynamodb.Table('t_loan_pay')
        filtering_exp = Key('loan_id').eq(loan_id)
        filtering_exp2 = Key('trans_id').eq(trans_id)
        loan_pay_rec = pay_table.scan(FilterExpression=filtering_exp and filtering_exp2)['Items']
        # loan_rec = table.query(KeyConditionExpression=Key('loan_id').eq(loan_id) & Key('trans_id').eq(trans_id))
        return loan_pay_rec
    	
