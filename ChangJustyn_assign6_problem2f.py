"""
Assignment 6, Part 2f
Justyn Chang
"""
#place all previous functions into one module
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
def plus(width, char):
    mid = ""
    for i in range(width):
        mid += char
    if width % 2 == 0:
        vert1 = ""
        width = (width - 1)//2
        for i in range(1, 2):
            vert1 += ((" " * width) + (char))
        vert = vert1 + char + "\n" + vert1 + char + "\n"
    if width % 2 != 0:
        vert = ""
        width = width - 1
        for i in range(1, 3):
            vert += ((" " * (width//2)) + (char + "\n"))
    plus = vert + mid + "\n" + vert
    return plus

def minus(width, char):
    mid = ""
    for i in range(width):
        mid += char
    minus = "\n" + "\n" + mid + "\n" + "\n" + "\n"
    return minus
def number_0(width, char):
    top = ""
    for i in range(width):
        top += char
    side = ""
    for i in range(1, 4):
        width1 = width - 2
        side += (char + (" " * width1) + (char + "\n"))
    bottom = ""
    for i in range(width):
        bottom += char
    zero = top + "\n" + side + bottom + "\n"
    return zero

def number_1(width, char):
    one = ""
    width = width - 1
    for i in range(1, 6):
        one += ((" " * width) + (char + "\n"))
    return one

def number_2(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    width1 = width - 1
    for i in range(5, 6):
        side1 += (" " * width1) + (char + "\n")
    side2 = ""
    for i in range(1, 2):
        side2 += (char + "\n")
    two = top + "\n" + side1 + top + "\n" + side2 + top + "\n"
    return two

def number_3(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    width1 = width - 1
    for i in range(5, 6):
        side1 += (" " * width1) + (char + "\n")
    three = top + "\n" + side1 + top + "\n" + side1 + top + "\n"
    return three

def number_4(width, char):
    side = ""
    for i in range(1, 3):
        width1 = width - 2
        side += (char + (" " * width1) + (char + "\n"))
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    width1 = width - 1
    for i in range(4, 6):
        side1 += (" " * width1) + (char + "\n")
    four = side + top + "\n" + side1
    return four

def number_5(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    width1 = width - 1
    for i in range(5, 6):
        side1 += (" " * width1) + (char + "\n")
    side2 = ""
    for i in range(1, 2):
        side2 += (char + "\n")
    five = top + "\n" + side2 + top + "\n" + side1 + top + "\n"
    return five

def number_6(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    for i in range(1, 2):
        side1 += (char + "\n")
    side2 = ""
    for i in range(1, 2):
        width1 = width - 2
        side2 += (char + (" " * width1) + (char + "\n"))
    six = top + "\n" + side1 + top + "\n" + side2 + top + "\n"
    return six

def number_7(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    width1 = width - 1
    for i in range(2, 6):
        side1 += (" " * width1) + (char + "\n")
    seven = top + "\n" + side1
    return seven

def number_8(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    for i in range(1, 2):
        width1 = width - 2
        side1 += (char + (" " * width1) + (char + "\n"))
    eight = top + "\n" + side1 + top + "\n" + side1 + top + "\n"
    return eight

def number_9(width, char):
    top = ""
    for i in range(width):
        top += char
    side1 = ""
    for i in range(1, 2):
        width1 = width - 2
        side1 += (char + (" " * width1) + (char + "\n"))
    side2 = ""
    width1 = width - 1
    for i in range(4, 6):
        side2 += (" " * width1) + (char + "\n")
    nine = top + "\n" + side1 + top + "\n" + side2
    return nine

def print_number(num, width, char):
    if num == 0:
        print(number_0(width, char))
    if num == 1:
        print(number_1(width, char))
    if num == 2:
        print(number_2(width, char))
    if num == 3:
        print(number_3(width, char))
    if num == 4:
        print(number_4(width, char))
    if num == 5:
        print(number_5(width, char))
    if num == 6:
        print(number_6(width, char))
    if num == 7:
        print(number_7(width, char))
    if num == 8:
        print(number_8(width, char))
    if num == 9:
        print(number_9(width, char))

def horizontal_line(width, char):
    pattern = ""
    for i in range(width):
        pattern += char
    return pattern

def vertical_line(shift, height, char):
    pattern = ""
    for i in range(height):
        pattern += ((" " * shift) + (char + "\n"))
    return pattern

def two_vertical_lines(width, height, char):
    pattern = ""
    width = width - 2
    for i in range(height):
        pattern += (char + (" " * width) + (char + "\n"))
    return pattern
