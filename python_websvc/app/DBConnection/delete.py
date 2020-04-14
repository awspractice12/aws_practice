from connectionManager import connectionManager as conn


dynamodb = conn.ddbres

table = dynamodb.Table('t_loan')

table.delete()

table = dynamodb.Table('t_loan_pay')

table.delete()