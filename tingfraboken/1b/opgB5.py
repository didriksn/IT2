num = int(input("Enter a number: "))

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