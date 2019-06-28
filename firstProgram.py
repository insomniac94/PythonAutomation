import os
'''
Written by: Brandon Hough

This program will ask the user for thier name and age.
Then print out some results to the screen based on the input.

Note: Commenting your code is nice for be able to refrence your code
later, or if someone else wants to use it. Excessive commenting is not
necessary though for simple code.
'''

# clear the screen
os.system('cls')

# storing the users name into the variable user_name
user_name = input('What is your name? ')

# storing the users age into the variable user_age
user_age = input('What is your age? ')

# Priting a message to the user with their name at the end
print('Hello, it is nice to meet you '+  str(user_name) +  '!')

# Printing the length of the users name
print('The length of your name is ' + str(len(user_name)) + ' characters!')

# Priting how old the user will be in a year from now
print('You will be ' + str(int(user_age) + 1) + ' in 1 year.')

