#Exercise 6: Brute Force Attack - Basic

#defining a variable to enter a password 
crct_password = 12345

#using while loop 
while True: 
  user_password = int(input("Enter your Password : ")) #asking an input from the user 

  if user_password == crct_password:
    print("The Password is Correct , Congrats ")
    break  #if the password given by the user correct , then the loop will break 
  else: 
    #if the password given by the user is not correct , then the loop will continue until and unless the correct password is given
    print ("The password is Incorrect , Please Try again") 