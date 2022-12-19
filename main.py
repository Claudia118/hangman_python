import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

#Get user name
name = input("Enter your name: ")
print("Hello", name, "let's play")

def question():
    question = input("Enter  “Yes” or “No” question that you’d like to ask the Magic 8-Ball : ")
    print(answers[random.randint(0, len(answers) - 1)])
    replay()

#Askng user if they want to ask another question
def replay():
    try_again = input('Do you have another question? [YES/NO] ').upper()
    if try_again == "YES":
        question()
    elif try_again == "NO":
        exit()
    else:
        print('I apologies, I did not catch that. Please try again.')
        replay()


question()

