#asking a input from the user
salary = int (input ("Please Enter your Salary :"))
commission = 0 #commission is set to zero as it will increase depending on the persons salary
if salary >  5000:
     commission = 150
     print("Congrats on the commission amout")
else :
    commission = 0
    print("You have no commission amount to revieve")
#this will add up the commissions
print ("Your Commission is "+str(commission))