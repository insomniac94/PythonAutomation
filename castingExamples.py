import os
'''
Written by: Brandon Hough
'''

os.system('cls')

# Here are the three types of casting you will use

print("-" * 15, "Integer Casting", "-" * 15)
print(7 + int('598'))
print("")

print("-" * 15, "String Casting", "-" * 15)
print('Name: Alice' + ' | Age:' + str(' 21'))
print("")

print("-" * 15, "Floating Point Casting", "-" * 15)
print(8.25 + float('5.7'))
print("")

# Here is an additional function that is very useful
# Google 'Python Built-In Functions' for more
print("-" * 15, "Rounding Function", "-" * 15)
print(round(5.7))