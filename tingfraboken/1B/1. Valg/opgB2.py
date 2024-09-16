num = int(input("Enter a number: "))

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