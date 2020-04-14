from flask import Flask, jsonify
from Services.loan_services import *
from datetime import datetime
import loan_calc
import re

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

# d = datetime.datetime.today()
dt = datetime.date(datetime.now())

cust_id = str(input("Customer ID: "))
loan_id = str(input("Loan ID: "))

loan_rec = loan_retrive.retrieveloan(cust_id, loan_id)
if loan_rec['Items'][0]['loan_status'] == "A":
    print ("Account is Active")
else:
    print ("Account is Inactive")
    exit()

principal_amount = loan_rec['Items'][0]['principal_amount']
rate_of_interest = loan_rec['Items'][0]['rate_of_interest']
loan_duration = int(loan_rec['Items'][0]['loan_duration'])
trans_date = (dt.strftime('%d-%m-%Y'))
#Monthly Payment Calculation
monthly_payment = loan_calc.monthly_loan(principal_amount,rate_of_interest,loan_duration)

print ('Current date and time:', trans_date)

print("Loan amount: ",principal_amount," Interest rate: ",rate_of_interest)

print("Duration (Years): ",loan_duration," Monthly payment: ",int(monthly_payment))
installment_amt = monthly_payment
trans_id = int(input('Transaction ID:'))
installment_no = int(input('Installment:'))
Pay_Sel = str(input('Enter Y To Continue Payment:'))

if Pay_Sel == "Y":
    if loan_rec['Items'][0]['loan_status'] == "A":
        loan_payment.loan_payment(loan_id,trans_id,trans_date,installment_no,installment_amt)
    
# pay_rec = payment_retrive.retrieve_loan_pay(loan_id, trans_id)   
# # print (pay_rec)
# print (pay_rec['Items'][0]['loan_id'])
# print (pay_rec['Items'][0]['trans_id'])
# print (pay_rec['Items'][0]['trans_date'])
# print (pay_rec['Items'][0]['installment_no'])
# print (pay_rec['Items'][0]['installment_amt'])


pay_rec = payment_retrive.retrieve_cust_pay(loan_id)   
# print (pay_rec)
for x in pay_rec['Items']:
    print(x)
    # print (pay_rec['Items'][0]['installment_amt'])

# for x in range(1,loan_duration+1):
#     mon = x*12
#     rem = loan_calc.remaining_bal(principal_amount,rate_of_interest,loan_duration,mon)
#     print("Year: ",x," Balance remaining: ",int(rem)," Total payments: ",int(monthly_payment*mon))



