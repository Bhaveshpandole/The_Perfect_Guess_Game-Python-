#random is a Builtin module
import random

#random.randint is a method select number between (start, end)
n = random.randint(1, 100)

#a is already asign -1 because we want to satisfied this while() condition to run forward
a = -1
guesses = 1

#Conditional expression
while(a != n):

    #a is taking inpute from user
    a = int(input("Guess the number: "))

    #conditional expression
    if(a>n):
        #statement
        print("Lower number please!")

        #increement
        guesses += 1
        
    elif(a<n):
        print("Higher number please!")
        guesses += 1

#result print as a statement
print(f"You have guessed the number {n} correctly in {guesses} attempts.")
