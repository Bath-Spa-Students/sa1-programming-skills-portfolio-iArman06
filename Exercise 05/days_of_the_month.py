#Exercise 5: Days of the Month

#"days_in_month" is a variable which is declared to store the month numbers on left and its respective month days
days_in_month = days_in_month = {
                                 1: 31,  # January
                                 2: 28,  # February (doesn't account for Leap year)
                                 3: 31,  # March
                                 4: 30,  # April
                                 5: 31,  # May
                                 6: 30,  # June
                                 7: 31,  # July
                                 8: 31,  # August
                                 9: 30,  # September
                                 10: 31, # October
                                 11: 30, # November
                                 12: 31  # December
}  #dictionary 


#Now we will ask the user to input a number between 1 and 12 which represents the month 
month = int(input("Enter a Number between 1 - 12 : ")) #month is a variable which will hold the users input 

#Result
#using if else statement to give result according to the users input
if 1<= month <=12:

    #if the user inputs a number beteeen 1 and 12 , then the statememnt below will be printed
    print(f'The number of days in month {month} is {days_in_month[month]}.') 
else: 
    #if the user inputs a number that isn't between 1 and 12 , then the statememnt below will be printed
    print ("Invalid month number. Please enter a number between 1 and 12.")
