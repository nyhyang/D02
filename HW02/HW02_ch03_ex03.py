#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def main_line():
	print('+ - - - - ')

def side_line():
	print('|        ')

def main_lines():
	do_twice(main_line)
	print('+')

def side_lines():
	do_twice(side_line)
	print('|')

def print_row():
	main_lines()
	do_four(side_line）

def print_grid():
	do_twice(print_row)
	main_lines()

print_grid()















# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    
print_grid()



if __name__ == "__main__":
    main()