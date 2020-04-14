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
        dynamodb = conn.ddbcln
        return dynamodb.scan(
        TableName='t_loan'
        )

    def retrievecust(cust_id):
        dynamodb = conn.ddbres
        table = dynamodb.Table('t_loan')
        customer = table.query(KeyConditionExpression=Key('cust_id').eq(cust_id))
        return customer
          
    def retrieveloan(cust_id,loan_id):
    	dynamodb = conn.ddbres
    	table = dynamodb.Table('t_loan')
    	loan_rec = table.query(KeyConditionExpression=Key('cust_id').eq(cust_id) & Key('loan_id').eq(loan_id))
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
        dynamodb = conn.ddbcln
        return dynamodb.scan(
        TableName='t_loan_pay'
        )

    def retrieve_cust_pay(loan_id):
    	dynamodb = conn.ddbres
    	table = dynamodb.Table('t_loan_pay')
    	pay_det = table.query(KeyConditionExpression=Key('loan_id').eq(loan_id))
    	return pay_det

    def retrieve_loan_pay(loan_id,trans_id):
    	dynamodb = conn.ddbres
    	table = dynamodb.Table('t_loan_pay')
    	loan_rec = table.query(KeyConditionExpression=Key('loan_id').eq(loan_id) & Key('trans_id').eq(trans_id))
    	return loan_rec
    	
