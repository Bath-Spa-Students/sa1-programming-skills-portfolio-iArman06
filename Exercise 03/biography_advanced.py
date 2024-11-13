#Exercise 3: Biography - Advanced Requirement

user_name = input("Enter your Name :")          #user_name is a variable which will hold the users answer 
user_hometown = input("Enter your Hometown :")  #user_hometown is a variable which will hold the users answer 

try: #Python will attempt this line of code 
    age= int(input("Enter your age :"))         #age is a variable which will hold the numeric age of the user 
except ValueError:
    #if the user enters a string value then the line of code will be executed stating invalid input 
    print("The Input is Invalid , The Age must be a numeric number") 
    age= None #this line of code will be executed if the Input is Invalid


#now we will store the value given by the user into an Dictonary 
user_info = { 
    "Name" : user_name ,
    "Hometown" : user_hometown ,
    "age" : age} #dictonary

#result
#we are using the Triple quotes format in f-string for multiline format
print (f"""Name : {user_info['Name']}       
       Hometown : {user_info['Hometown']}
       Age : {user_info['age']}""")