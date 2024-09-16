# Skrevet ved hjelp av github copilot


import random

print("Welcome to the Fun Silly Useless Machina!")
print("Please enter your name:")
name = input()

print("Hello,", name, "!")
print("I'm here to provide you with some fun and silliness.")

# Let's generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Let's generate a random silly message based on the random number
silly_messages = [
    "You are the champion of silliness!",
    "You have been officially certified as a silly person.",
    "Silliness level: maximum!",
    "Warning: excessive silliness detected!",
    "Congratulations! You have reached the pinnacle of silliness.",
    "Silly mode activated!",
    "Silliness overload!",
    "Silly alert! Silly alert!",
    "Silliness level: off the charts!",
    "You are the silliest person in the universe!"
]

silly_message = random.choice(silly_messages)

print("And the result of our silliness calculation is...")
print(silly_message)