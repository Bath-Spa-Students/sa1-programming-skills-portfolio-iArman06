#Primitive Quiz

correct_answer = "Paris" #correct_answer is a variable which holds the actual answer of the question

#question asked to the person 
answer = input ("What is the capital of France? : ") 
#answer is a Variable which will hold the answer given by the user

#Result
#Using If else statement to print statements according to answers given by the user
if answer == correct_answer:
    print ("The answer is Correct") 
    #This statetment will be printed If the answer given is Paris
else:
    print (f"The answer is Incorrect, The actual answer is {correct_answer}") 
    #This statetment will be printed If the answer given is not Paris