#Exercise 6: Brute Force Attack - Optional

#defining a variable to enter a password 
crct_password = 12345
total_attempts = 5 #the variable will hold the maximum attempts allowed to enter the correct password
counter = 0 #this variable will count the attempts done 


#using while loop 
while counter < total_attempts: 
  user_password = int(input("Enter your Password : ")) #asking an input from the user 

  if user_password == crct_password:
    print("The Password is Correct , Congrats ")
    break  #if the password given by the user correct , then the loop will break 
  else: 
    counter += 1 # using += 1 , for incrementing in every wrong input
    remaining_chance = total_attempts - counter #remaining_chance will hold the total chances after each wrong input

    if remaining_chance > 0: 
       print(f"The pasword entered is wrong , You have {remaining_chance} attempts left")
    else:
     #will be printed once all the 5 attempts are over
      print("The maximum attempts have been done. You have no more access") 