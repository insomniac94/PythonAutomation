import os

'''
Written by: Brandon Hough

In programming you can use all arithmetic operators to perform operations.
Here are some examples of how to do so:
'''

# clears the screen each time the program is ran
# you must import os as shown on line 1
os.system('cls')

print("-" * 15,"Exponents", "-" * 15)
print("2^3 =", 2 ** 3)
print("5^121 =", 5 ** 42)
print("")

print("-" * 15, "Modulous or remainder", "-" * 15)
print("6 % 2 =", 6 % 2)
print("2 % 6 =", 2 % 6)
print("4096 % 13 =", 4096 % 13)
print("")

print("-" * 15, "Integer division/floored quotient (drops the decimal)", "-" * 15)
print("22 // 8 =", 22 // 8)
print("")

print("-" * 15, "Division", "-" * 15)
print("1857 / 10 =", 121 / 10)
print("")

print("-" * 15, "Multiplication", "-" * 15)
print("82 * 11 =", 82 * 11)
print("")

print("-" * 15, "Subtration", "-" * 15)
print("151651 -18189 =", 151651 - 18189)
print("")

print("-" * 15, "Addition", "-" * 15)
print("897984 + 489485 =", 897984 + 489485)
print("")

print("-" * 15, "Expression Evaluation", "-" * 15)
print("((8+16)*(9-15)//(2**3))/4 =", (((8+16)*(9-15)//(2**3))/4))
print("")

# Python will only accept valid infix/postfix expressions
# Line 52 will cause an error
print("-" * 15, " Invalid Expression Evaluation", "-" * 15)
print("45 + 5 + * 2 =", 45 + 5 + * 2)
print("")