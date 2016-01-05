def main():
    netPay()
def netPay():
    ratePerHour = int(input("Enter rate per hour: "))
    numberOfHours = int(input("Enter number of hours: "))
    percentage = int(input("Enter percentage: "))
    grossPay = ratePerHour * numberOfHours
    withholdingAmount = grossPay - percentage
    net = grossPay - withholdingAmount
    print ("Gross: {}".format(grossPay))
    print ("Width Holding Amount: {}".format(withholdingAmount))
if __name__ == '__main__':
    main()