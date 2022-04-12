"""
Assignment 6, Part 2g
Justyn Chang
"""
#ask how many problems to be completed and validate
problems = int(input("How many problems would you like to attempt? "))
while problems <= 0:
    print("Invalid number, try again")
    print()
    problems = int(input("How many problems would you like to attempt? "))

#ask for width of numbers and validate
width = int(input("How wide do you want your digits to be? 5-10: "))
while width <= 4 or width >= 11:
    print("Invalid width, try again")
    print()
    width = int(input("How wide do you want your digits to be? 5-10: "))
print()

#ask for type of character and validate
char = input("What character would you like to use? ")
while len(char) >= 2:
    print("String too long, try again")
    char = input("What character would you like to use? ")
print()

print("Here we go!")
print()
print("What is .....")
print()

#import modules
import random
import ChangJustyn_assign6_problem2f

#create for loop to answer as many problems as inputted above
correct = 0
wrong = 0
for i in range(problems):
    #generate random numbers and operator
    num1 = random.randint(0, 9)
    operator = random.randint(1, 2)
    num2 = random.randint(0, 9)

    #print random numbers and operator
    ChangJustyn_assign6_problem2f.print_number(num1, width, char)
    if operator == 1:
        print(ChangJustyn_assign6_problem2f.plus(width, char))
        oper = "+"
    if operator == 2:
        print(ChangJustyn_assign6_problem2f.minus(width, char))
        oper = "-"
    ChangJustyn_assign6_problem2f.print_number(num2, width, char)
    #have user input a guess for the correct answer
    ans = int(input("= "))
    #check inputted answer and tell if it is correct or not
    check = ChangJustyn_assign6_problem2f.check_answer(num1, num2, ans, oper)
    if check == True:
        print("Correct!")
        correct += 1
        print()
    if check == False:
        print("Sorry, that's not correct.")
        wrong += 1
        print()
#tell user how many they got right out of the total number of problems
total = correct + wrong
print("You got", correct, "out of", total, "correct!")
    
