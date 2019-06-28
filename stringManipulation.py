import os
'''
Written by: Brandon Hough
'''
# clears the screen each time the program is ran
# you must import os as shown on line 1
os.system('cls')

# you can concatenate, or conbine two strings together
first_name = 'Bob'
last_name = 'Burgers'
print(last_name , ", " , first_name)

# you can also use the '+' symbol to concatenate strings
# I like this one better than the comma because it will not
# add an extra space
print(last_name + ", " + first_name)

# You cannot concatenate a string and an integer,
# unless you cast the integer to a string.
# Casting is making the complier thing the data type
# you cast a value to another data type.
# print("Bill" + 42) <-- does not compile
print("Bill" + str(42))

# As you've seen me do in the last python files, you can multiply
# a string by a value to have it print several times
print('PrintThis ' * 3)

# You cannot multiply two strings
# print('Alice' * 'Bob) <-- does not compile

# You can only multipl a string by an integer, cannot be a floating point
# print('Alice' * 5.0) <-- does not compile
 