import os

def collatz(number):
    # if the number is even
    if number % 2 == 0:
        even_num = number // 2
        print(even_num )
        return even_num 
    # else number is odd
    else:
        odd_num = 3 * number + 1
        print(odd_num)
        return odd_num

def get_user_input():
    user_num = input("Enter a number: ")
    if user_num.isdigit() == False:
        print("Please enter valid input!")
        get_user_input()
    if user_num.isdigit() == True:
        check_num = collatz(int(user_num))
        if check_num != 1:
            print("Try again...")
            get_user_input()
        else:
            print("You got it!")

def main():
    os.system('cls')
    get_user_input()

# run main
if __name__ == '__main__':
    main()