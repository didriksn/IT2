import random

# 1b

num = int(input("Enter a number: "))


# 1)
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2)
if num > -1 and num < 10:
    print("The number is between 0 and 10.")
elif num >= 10 and num < 100:
    print("The number is between 10 and 100.")
elif num >= 100 and num < 1000:
    print("The number is between 100 and 1000.")
elif num >= 1000 and num < 10000:
    print("The number is between 1000 and 10000.")
else:
    print("The number is greater than or equal to 10000.")

# 3)
if num > 50 and num < 100:
    print("The number is between 50 and 100.")
else:
    print("The number is not between 50 and 100.")


# 5)
if num >= 0:
    if num > 100:
        print("The number is greater than 100 and positive.")
    else:
        print("The number is less than or equal to 100 and positive.")
else:
    if num < -100:
        print("The number is less than -100 and negative.")
    else:
        print("The number is greater than or equal to -100 and negative.")



# 6)
# <= betyr at noe er mindre enn eller lik noe annet. Det motsatte av dette ville vært > som betyr at noe er større enn noe annet.



# 7)
# == betyr at noe er likt noe annet. != betyr at noe ikke er likt noe annet.



# 8)
# problemet er at man må bruke == og ikke = i denne sammenhengen.



# 9)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
num4 = int(input("Enter a fourth number: "))
num5 = int(input("Enter a fifth number: "))

set = [num1, num2, num3, num4, num5]

if num1 == num2 == num3 == num4 == num5:
    print("All the numbers are equal.")
# 10)
else:
    print(max(set), "is the highest number.")


# 11)
# a == 0 and b == 0


# 12)
# a != 0 or b != 0


# 13)
# if a % 2 == 0:
#     print("a is an even number.")
# 14)
# else:
#     print("a is an odd number.")


# 15)
karakter = int(input("Skriv inn poengsummen din (0-100): "))

if karakter >= 0 and karakter <= 20:
    print("Du fikk karakteren 1.")
elif karakter >= 21 and karakter <= 40:
    print("Du fikk karakteren 2.")
elif karakter >= 41 and karakter <= 60:
    print("Du fikk karakteren 3.")
elif karakter >= 61 and karakter <= 80:
    print("Du fikk karakteren 4.")
elif karakter >= 81 and karakter <= 90:
    print("Du fikk karakteren 5.")
elif karakter >= 91 and karakter <= 100:
    print("Du fikk karakteren 6.")
else:
    print("wtf hvordan fikk du en karakter som er høyere enn 100 eller lavere enn 0 blud hacker")


# 16)
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print("Player chose:", player_choice)
print("Computer chose:", computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    print("Player wins!")
else:
    print("Computer wins!")

# 17)
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