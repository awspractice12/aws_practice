from flask import Flask, jsonify
from Services.loan_services import loan_entry as dbHandler
import loan_calc
import re


cust_id = str(input("Customer ID: "))
loan_id = str(input("Loan ID: "))
granted_date = str(input("Loan Date: "))
principal_amount = float(input("total loan amount taken: "))
rate_of_interest = float(input("annual interest rate applied: "))
loan_duration = int(input("loan duration in years: "))
loan_status = str(input("Loan Status: "))

#Monthly Payment Calculation
monthly_payment = loan_calc.monthly_loan(principal_amount,rate_of_interest,loan_duration)

dbHandler.loan_load(cust_id,loan_id,granted_date,principal_amount,rate_of_interest,loan_duration,monthly_payment,loan_status)


