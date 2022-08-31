import random

def magic8ball():
    response = input("(Press 'any key' for answer and 'quit' to exit)\nWhat is your question?\n")
    Eightball_answers = [
        "It is certainly",
        "It is decidely so",
        "Without a doubt",
        "Yes definately",
        "You may rely on it",
        "As I see it, yes",
        "Ask again later",
        "I better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook no so good",
        "Very doubtful"
        ]
    
    if response == "quit":
        print("Have A Good Day!")
    else:
        print(random.choice(Eightball_answers), "\n")
        magic8ball()

magic8ball()