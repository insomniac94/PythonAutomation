import os
'''
Written by: Brandon Hough

There are 3 main data types in Python; Integers, Floating Point Number,
and strings
'''

os.system('cls')

# Integers are whole numbers, here I have printed a list
# of integers from 0-4
print("-" * 15, "Integers", "-" * 15)
int_nums = [-2, -1, 0, 1, 2] 
print(str(int_nums)[1:-1])
print("")

# Floating point numbers are decimal numbers, here I have 
# printed a list of floating point number examples
print("-" * 8, "Floating Point Numbers", "-" * 8)
fp_nums = [-2.5, -1.745, 0.75, 1.425, 2.689] 
print(str(fp_nums)[1:-1])
print("")

# Strings is a sequence characters or numbers
# You can use single or double quotes, depending if you have
# a ' in the string or not
print('-' * 16, 'Strings', '-' * 16)
string_ex = 'Hello. My favorite number is 7!'
print(string_ex)
print("")

# if you can an error that says EOL while scanning string literal,
# you probably forgot a starting or ending ' or " to the string
# Ex: print('This will not work)