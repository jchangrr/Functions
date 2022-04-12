"""
Assignment #6, Part 1
Justyn Chang
"""
# function:   get_input
# input:      a prompt to ask the user (String), a low value (integer) and a high value (integer)
# processing: continually prompts the user with the supplied prompt for an integer. if the
#             user does not supply an integer within the defined range the function will re-prompt them
# output:     returns the integer the user supplied
def get_input(string, low, high):
    num = int(input(string))
    while True:
        if num < low:
            print("Invalid integer, try again.")
            num = int(input(string))
        elif num > high:
            print("Invalid integer, try again.")
            num = int(input(string))
        else:
            break
    return num

# function: compute_area_of_rectangle
# input: length (integer) and width (integer)
def compute_area_of_rectangle(length, width):
    # processing: computes the area of the described rectangle
    area = length * width
    # output: returns the area of the described rectangle (integer)
    return area

# function: compute_perimeter_of_rectangle
# input: length (integer) and width (integer)
def compute_perimeter_of_rectangle(length, width):
    # processing: computes the perimeter of the described rectangle
    perimeter = (2 * length) + (2 * width)
    # output: returns the perimeter of the described rectangle (integer)
    return perimeter

# function:   draw_rectangle
# input:      length (integer) and width (integer)
# processing: constructs the rectangle using a series of "*" characters
# output:     returns the rectangle (string)
def draw_rectangle(length, width):
    side1 = "*" * width + "\n"
    rect = side1 * length
    return rect
    
length = get_input("Enter a length between 3 and 10", 3, 10)
width  = get_input("Enter a width between 3 and 10", 3, 10)

area  = compute_area_of_rectangle(length, width)
perim = compute_perimeter_of_rectangle(length, width)

print ("Area:", area, "; Perim:", perim)

rect = draw_rectangle(length, width)
print (rect)
