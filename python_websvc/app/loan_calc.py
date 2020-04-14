# ---function for monthly loan amount calculation---
def monthly_loan(principal_amount,rate_of_interest,loan_duration):
    n = loan_duration*12 #total number of months
    r = rate_of_interest/(100*12) #interest per month
    monthly_payment = principal_amount*((r*((r+1)**n))/(((r+1)**n)-1)) #formula for compound interest applied on mothly payments.
    return monthly_payment

# ---funtion for remaining loan balance calculation---
def remaining_bal(principal_amount,rate_of_interest,loan_duration,payments):
    r = rate_of_interest/1200 # monthly interest rate
    m = r + 1
    n = loan_duration*12 # duration in months
    
    # remaining balance using compound interest formula
    remaining = principal_amount*(((m**n)-(m**payments))/((m**n)-1))
    return remaining

