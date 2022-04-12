"""
Assignment 6, Part 2d
Justyn Chang
"""
# functions: plus and minus
# input: a width value (integer) and a single character (string)
# processing: creates plus or minus operator sign based on inputs
# output: returns plus or minus operator
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

