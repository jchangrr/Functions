"""
Assignment 6, Part 2e
Justyn Chang
"""
# function: check_answer
# input: two numbers to add or subtract (integers), an inputted answer (integer), and an operator sign
# processing: adds or subtracts the two numbers together based on operator and checks if result is the same as the inputted answer
# output: returns True or False
def check_answer(num1, num2, ans, oper):
    if oper == "+":
        ans1 = num1 + num2
        if ans1 == ans:
            answer = True
            return answer
        if ans1 != ans:
            answer = False
            return answer
    if oper == "-":
        ans1 = num1 - num2
        if ans1 == ans:
            answer = True
            return answer
        if ans1 != ans:
            answer = False
            return answer
