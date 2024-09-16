# Lag et program som leser inn en tekst fra brukeren, og som skriver ut teksten med én bokstav per linje.


def nyBokstavPerLinje():
    inta = input("Skriv en setning: ")
    letter = [x for x in inta]

    for i in letter:
        print(i)


nyBokstavPerLinje()