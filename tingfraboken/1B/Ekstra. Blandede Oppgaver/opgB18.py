mal = input("Skriv inn maleenheten din (Celsius ('C'), Fahrenheit ('F'), Kelvin ('K')): ").lower()
temp = float(input("Skriv inn temperaturen: "))

if mal == "c":
    print("Temperaturen i Fahrenheit er", (temp * 9/5) + 32)
    print("Temperaturen i Kelvin er", temp + 273.15)
elif mal == "f":
    print("Temperaturen i Celsius er", (temp - 32) * 5/9)
    print("Temperaturen i Kelvin er", (temp - 32) * 5/9 + 273.15)
elif mal == "k":
    print("Temperaturen i Celsius er", temp - 273.15)
    print("Temperaturen i Fahrenheit er", (temp - 273.15) * 9/5 + 32)