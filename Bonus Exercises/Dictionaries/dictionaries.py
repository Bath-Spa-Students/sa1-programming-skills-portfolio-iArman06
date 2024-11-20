#Use a dictionary to store information about a person you know.Store their first name,
#last name, age, and the city in which they live.

#You should have keys such as first_name, last_name, age, and city. Print each piece of
#information stored in your dictionary.

#making a dictionary 
#"person" is a variable which holds the dictionary
person = { "First_name" : "Arman" , 
           "Second_name" : "Hossain" , 
           "Age" : 18 ,
           "City" : "Abu Dhabi" } 


#printing part/result
#now we will print each piece of information separately 
print(f"The First Name of the Person is {person['First_name']}")
print(f"The Second Name of the Person is {person['Second_name']}")
print(f"The Age of the Person is {person['Age']}")
print(f"The City where the Person lives is {person['City']}")
