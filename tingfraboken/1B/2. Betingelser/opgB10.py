num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
num4 = int(input("Enter a fourth number: "))
num5 = int(input("Enter a fifth number: "))

set = [num1, num2, num3, num4, num5]

if num1 == num2 == num3 == num4 == num5:
    print("All the numbers are equal.")
else:
    print(max(set), "is the highest number.")