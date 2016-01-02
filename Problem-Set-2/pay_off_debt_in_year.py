balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
minimumpayment = 0
originalbalance = balance

while balance >= 0:
    minimumpayment += 10
    for x in range (1, 13):
        balance = (balance - minimumpayment) + ((balance - minimumpayment) * monthlyInterestRate)
    if balance >= 0:
        balance = originalbalance

print "Lowest Payment: " + str(minimumpayment)
