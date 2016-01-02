balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/ 12.0
totalpaid = 0
for month in range(1, 13):
    minimumpayment = monthlyPaymentRate * balance
    balance = (balance - minimumpayment) + ((balance - minimumpayment) * monthlyInterestRate)
    totalpaid += minimumpayment
    print "Month: " + str(month)
    print "Mininum monthly pament: " + str(round(minimumpayment, 2))
    print "Remaining balance: " + str(round(balance, 2))
print "Total paid: " + str(round(totalpaid, 2))
print "Remaining balance: " + str(round(balance, 2))
