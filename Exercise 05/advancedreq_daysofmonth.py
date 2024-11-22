#Exercise 5 : Advanced Requirement

#"days_in_month" is a variable which is declared to store the month numbers on left and its respective month days
#Dictionary
days_in_month = days_in_month = {
                                 1: 31,  # January
                                 2: 29,  # February (account for Leap year)
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
} 


#Now we will ask the user to input a number between 1 and 12 which represents the month 
month = int(input("Enter a Number between 1 - 12 : ")) #month is a variable which will hold the users input 

#Result
#using if else statement to give result according to the users input
if 1<= month <=12:

    if month == 2: #February
        year_of_leap = input("Is the Year a Leap Year :").lower() 
        #lower() function will convert the users input to Lower case to avoid the capitalization problem

        if year_of_leap == "yes" :
            print (f'The number of days in month {month} is 29 days') #if the year is a leap year then this statement will be printed 
        else:
            print (f'The number of days in month {month} is 28 days') #if the year is a not a leap year then this statement will be printed 
    else:
    #the statememnt below will be printed for others months which is not February
        print(f'The number of days in month {month} is {days_in_month[month]}.') 
else: 
    #if the user inputs a number that isn't between 1 and 12 , then the statememnt below will be printed
    print ("Invalid month number. Please enter a number between 1 and 12.")
