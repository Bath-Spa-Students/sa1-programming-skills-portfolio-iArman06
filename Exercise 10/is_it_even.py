# Exercise 10: Is it even?


#The program should ask the user for a number from within the main function.
#declaring a function to check if the number entered is even or odd 
def even_or_odd(numb):
    if numb % 2 == 0:  #number divided by 2 determines if the entered number is a even number or odd
        return ("The number is an Even Number ") #will be printed if the number is even 
    else:
        return ("The number is an Odd number ") #will be printed if the number is odd
    
#The entered number should be passed to a function that determines if the value is even or odd.
def main():
        user_numb = int(input("Enter a Numeric Number :"))   #asking the user to input a number which will be stored in "user_numb"


        result = even_or_odd(user_numb) #passing the entered number to the function we declared above
        print(result) #result gets printed saying if the entered number is even or odd

if __name__ == "__main__":
    main() #starts the program by calling main function
        
