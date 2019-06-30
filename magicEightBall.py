import random, os

messages = ['It is certain',
           'It is decidedly so',
           'Yes definetly',
           'Reply hazy try again',
           'Ask again later',
           'Concetrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful']

os.system('cls')
question = input("What is your question for the 8 ball? ")
print("8 Ball Response: " + messages[random.randint(0, len(messages)-1)])