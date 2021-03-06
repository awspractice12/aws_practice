from flask import Flask, jsonify
from Services.loan_services import *
from decEncoder import *
import decimal
import json


app = Flask(__name__)

@app.route('/')
def index():
    return "This is the main page."

@app.route('/get-all-loans')
def get_all_loans():
    return jsonify(loan_retrive.get_all_loans())

@app.route('/get-cust-loan/<cust_id>',methods=['GET'])
def get_cust_loan(cust_id):
    customer = loan_retrive.retrievecust(cust_id)
    customer = json.dumps((customer), indent=4, cls=DecimalEncoder)
    return json.loads(customer)

@app.route('/get-loan/<cust_id>/<loan_id>',methods=['GET'])
def get_loan(cust_id,loan_id):
    customer = loan_retrive.retrieveloan(cust_id,loan_id)
    customer = json.dumps((customer), indent=4, cls=DecimalEncoder)
    return json.loads(customer)


@app.route('/get-all-pay')
def get_all_pay():
    return jsonify(payment_retrive.get_all_pay())

@app.route('/get-cust-pay/<loan_id>',methods=['GET'])
def get_cust_pay(loan_id):
    cust_loan = payment_retrive.retrieve_cust_pay(loan_id)
    cust_loan = json.dumps((cust_loan), indent=4, cls=DecimalEncoder)
    return json.loads(cust_loan)

@app.route('/get-pay/<loan_id>/<trans_id>',methods=['GET'])
def get_pay(loan_id,trans_id):
    cust_loan = payment_retrive.retrieve_loan_pay(loan_id,trans_id)
    cust_loan = json.dumps((cust_loan), indent=4, cls=DecimalEncoder)
    return json.loads(cust_loan)

@app.route('/get-customer/<cust_id>',methods=['GET'])
def get_customer(cust_id):
    cust_loan = payment_retrive.retrieve_loan_pay(loan_id,trans_id)
    cust_loan = json.dumps((cust_loan), indent=4, cls=DecimalEncoder)
    return json.loads(cust_loan)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
