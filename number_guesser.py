import random
import time

def slow_print(text):
    for char in text:
        print(char, end = '', flush = True)
        time.sleep(0.1)
    print() 

slow_print("Hello there!")
slow_print("I'm a sentient AI entity capable of reasoning and logic, created by Joseph Obukofe 😎")
slow_print("Just kidding, I'm a simple program created to do his bidding")
slow_print("PS: I'm pretty good at guessing numbers 👀")

name = input("Whats your name?: ")

slow_print(f"Hi! {name} 😊")
slow_print("That's a weird name but okay")
slow_print("I want you to think of a number between 1 and 100 and I'll try and guess it")

first_response = input("Kabish? (Yes/No): ")

if first_response == "Yes":
    slow_print("I thought so")
else:
    slow_print("Okay...")
    slow_print("Well that's on you")
    
slow_print("Anyways")
slow_print("Think of a number, it could be a floating point too. I'm that smart 🤓")
slow_print("Thought of a number yet ?")

second_response = input("Yes/No: ")

if second_response == "Yes":
    slow_print("Great 🤩")
else:
    slow_print("Alright...")
    slow_print("Take your time...or I will 🙂")
    slow_print("Just kidding 👀")
    third_response = input("I'm guessing you've come up with a number now? (Yes/No): ")

    if third_response == "No":
        slow_print("Not so bright are we, maybe I should guess a number for you 🙄")
    else:
        slow_print("Finally... ugh")

slow_print("Anyways...")
secret_number = input("What's your secret number? (Don't worry, I won't peek 😉): ")

slow_print("Ah, the mysteries of your mind! Now, watch as I use my complex algorithms to deduce your secret number...")

for _ in range(2):
    slow_print("Running algorithm...")
    time.sleep(2)
    slow_print("Analyzing data...")
    time.sleep(2)
    slow_print("Crunching numbers...")
    time.sleep(2)

slow_print(f"Aha! After all that complex analysis, I've determined that your secret number is... {secret_number}! 😄")
slow_print("Well, that was fun! Thanks for playing with me. If you want to try again, feel free to let me know!.")
time.sleep(3)
slow_print("Please don't")

    
    


