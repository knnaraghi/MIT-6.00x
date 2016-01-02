balance = 431015
annualInterestRate = 0.15
monthlyInterestRate = annualInterestRate / 12.0
minimumpayment = balance / 12.0
maximumpayment = (balance * (1+ monthlyInterestRate)**12) / 12.0
payment = (minimumpayment + maximumpayment) / 2.0
originalbalance = balance

while abs(balance) >= 0.01:
    balance = originalbalance
    payment = (minimumpayment + maximumpayment) / 2.0
    for x in range (1, 13):
        balance = (balance - payment) + ((balance - payment) * monthlyInterestRate)
    if balance == 0:
        break    
    if balance > 0:
        minimumpayment = payment
    if balance < 0:
        maximumpayment = payment
    

print "Lowest Payment: " + str(round(minimumpayment, 2))
