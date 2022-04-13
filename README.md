# Functions
For this program you completing a "rectangle simulator" program that will relies on four specially created functions. The full program has been written below - all you need to do is successfully write the four functions described here. Refer to the IPO notation below when writing these functions (note: you can just copy the IPO directly into your code to document your functions):

# function:   compute_area_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the area of the described rectangle
# output:     returns the area of the described rectangle (integer)

# function:   compute_perimeter_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the perimeter of the described rectangle
# output:     returns the perimeter of the described rectangle (integer)

# function:   draw_rectangle
# input:      length (integer) and width (integer)
# processing: constructs the rectangle using a series of "*" characters (see below for a sample 4 by 3 rectangle:)
#             ***
#             ***
#             ***
#             ***
# output:     returns the rectangle (string)

# function:   get_input
# input:      a prompt to ask the user (String), a low value (integer) and a high value (integer)
# processing: continually prompts the user with the supplied prompt for an integer. if the
#             user does not supply an integer within the defined range the function will re-prompt them
# output:     returns the integer the user supplied

Here's the main body of your program - you should be able to paste this code into your Python file and the program should run using your functions.

length = get_input("Enter a length between 3 and 10", 3, 10)
width  = get_input("Enter a width between 3 and 10", 3, 10)

area  = compute_area_of_rectangle(length, width)
perim = compute_perimeter_of_rectangle(length, width)

print ("Area:", area, "; Perim:", perim)

rect = draw_rectangle(length, width)
print (rect)

Part 2a:
For this step you will be writing three functions:
# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)

Part 2b:
Next, write 10 new functions that generate the digits 0-9 using your three line functions. The goal here is to render the digits as they would appear on a digital display:

Each function should accept a "width" argument to control how wide the number should be as well as a single character. You can assume numbers will always be printed with a height of 5.

Part 2c:
Write a function called 'print_number' that prints out any desired number to the screen. Here's the IPO for this function:

# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything

Part 2d:
Write two new functions that simulate the addition and subtraction operators. Each of these functions should accept a width value as an argument (integer) and a single character (string) -- the function should then return the generated pattern. You can assume the operators will always be 5 units high.

Part 2e:
Write a function called "check_answer" which will determine if a given addition or subtraction problem was solved correctly. Here's the IPO notation for the function:

# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct

Part 2f:
Move all of your functions into an external module. 

Part 2g:
Finally, put everything together and write a program that lets the user practice a series of random addition and subtraction problems. Begin by asking the user for a number of problems (only accept positive values) and a size for their numbers (only accept numbers between 5 and 10). Also prompt them for a single character to be used to generate their patterns - only accept single character strings (i.e. 'a' is OK, but 'apple' is not). The generate a series of random addition and subtraction problems - display the numbers to the user with your digital display functions. Then prompt the user for an answer and check the answer using your check_answer function. Your program should also keep track of how many correct questions the user answered during their game. 


