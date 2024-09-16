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
    print("karakter over 100 er invalid")
