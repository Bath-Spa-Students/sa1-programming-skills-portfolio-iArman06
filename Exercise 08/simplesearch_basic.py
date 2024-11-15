# Exercise 8: Simple Search - Basic

#Defining a list named name_list
name_list = ("Jake","Zac", "Ian", "Ron", "Sam", "Dave")

#Result
if "Sam" in name_list:
    print("The Name Sam is present in the List") #will be printed if the name is present in the list
else: 
    print("The Name Sam is not present in the list") #will be printed if the name isn't present in the list

#To know the position of Name Sam in the list we use the Indexing function 
place=name_list.index("Sam")  
 #In a list the Indexing starts from 0 , therefore the position of Sam will be 4 in the list
print(f"The position of Sam is at {place}")
