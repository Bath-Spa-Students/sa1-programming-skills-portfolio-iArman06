#Write a loop that prompts the user to enter a series of pizza toppings until they enter a
#'quit' value. As they enter each topping,
#Print a message saying you’ll add that topping to their pizza.

#will keep on asking the user about Pizza toppings unless he/she writes "quit"
print("Enter 'quit' when you are done adding your Pizza Toppings ")

#usig while loop
while True:
    #asking user the Pizza toppings which will be stored in the variable "pizza"
    pizza = input("Enter the Pizza Toppings as you like :")

    if pizza == 'quit':
        print("You are done adding toppings to your Pizza")
        break
    else:
        print(f"I will add that {pizza} to your pizza ")


