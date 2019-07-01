import os
'''
Written by: Brandon Hough

This program will take in a list of strings and puts a comma
and a space after each value. Also and before the last
string in the list.
'''

def add_comma():
    myString = ' '
    spam = ['apples', 'bananas', 'tofu', 'cats']
    for i in spam:
        if spam.index(i) < (len(spam)-1):
            myString = myString + i + ', '
        else:
            myString = myString + 'and ' + i

    return myString

def main():
    os.system('cls')
    myString = add_comma()
    print(myString)

# run main
if __name__ == '__main__':
    main()