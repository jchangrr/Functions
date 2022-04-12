"""
Assignment #6, Part 2a
Justyn Chang
"""
# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width, char):
    pattern = ""
    for i in range(width):
        pattern += char
    return pattern

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift, height, char):
    pattern = ""
    for i in range(height):
        pattern += ((" " * shift) + (char + "\n"))
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width, height, char):
    pattern = ""
    width = width - 2
    for i in range(height):
        pattern += (char + (" " * width) + (char + "\n"))
    return pattern

