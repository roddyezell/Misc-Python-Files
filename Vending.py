# Sales price is $0.20. Machine is given $1 bill. Function returns $0.80
# in change as 3 quarters and 1 nickel (fewest number of coins)
import math

def ChangeMaker(price, payment):

    print(price, payment)
    
    balance = payment - price
    change = [0] * 4

    # Payment is insufficient. Return customer's change.
    if (payment < price):
        balance = payment
    
    while (balance > 0):
        
        # Number of quarters
        if (balance >= 0.25):
            quarters = math.trunc(balance/0.25)
            change[3] = quarters
            balance = balance - (quarters*.25)
        # Number of dimes
        elif (balance >= 0.10):
            dimes = math.trunc(balance/.10)
            change[2] = dimes
            balance = balance - (dimes*.10)
        # Number of nickels
        elif (balance >= 0.05):
            nickels = math.trunc(balance/.05)
            change[1] = nickels
            balance = balance - (nickels*.05)
        # Number of pennies
        elif (balance >= 0.01):
            pennies = math.trunc(balance/.01)
            change[0] = pennies
            balance = balance - (pennies*.01)
        else:
            break
        
    return(change)
    
sales_price = float(input("Sales price: "))
submit_payment = 'N'
payment = []

while (sum(payment) < sales_price):
    submit_payment = input("Done adding money? (Y/N): ")
    if (submit_payment != 'N'):
        break
    else:
        temp_payment = (float(input("Payment amount: ")))
        payment.append(temp_payment)
        remaining = sales_price - sum(payment)

print(ChangeMaker(sales_price, sum(payment)))
