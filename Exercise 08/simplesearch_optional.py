# Exercise 8: Simple Search - Optional 

#Defining a list named name_list
name_list = ("Jake","Zac", "Ian", "Ron", "Sam", "Dave")

#asking user an input which will be stored in the variable name_search 
name_search = input("Enter the name of the Person you are looking for :")

#Result
if name_search in name_list: #lookig for the entered name in the list "name_list"
    #The statement below will be printed if the entered name is present in the defined list
    print(f"The given name {name_search} is present in the list {name_list}")
else:
    #The statement below will be printed if the Name entered is not present in the defined list
    print(f"The given name is not present in the list {name_list}")