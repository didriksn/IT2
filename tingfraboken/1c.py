'''

# 1 Bruk informasjonen om range() og skriv om koden ovenfor slik at utskriften blir
# A) tallene fra og med 1 til og med 30
for i in range(1,31):
    print(i)

# B) de første 100 partallene
for i in range(0, 100, 2):
    print(i)

# C) 5-ganger'n (fra og med 5 til og med 50)
for i in range(5, 51, 5):
    print(i)

# D) tallsekvensen 21, 28, 35, 42
for i in range(21, 43, 7):
    print(i)

# E) tallsekvensen 100, 90, 80, 70, 60, 50, 40, 30, 20, 10
for i in range(100, 0, -10):
    print(i)


# 2 hvilke sekvenser gir kodene nedenfor
# A) 0,1,2,3,4,5,6,7,8,9
# B) 1,2,3,4,5,6,7,8,9
# C) 1, 3, 5, 7, 9
# D) 10,9,8,7,6,5,4,3,2

'''

# 3 Lag et program som leser inn en tekst fra brukeren, og som skriver ut teksten med én bokstav per linje.

def nyBokstavPerLinje():
    inta = input("Skriv en setning: ")
    letter = [x for x in inta]

    for i in letter:
        print(i)
'''
nyBokstavPerLinje()
'''


# 4 Funksjonen print() har en parameter som heter end. I utangspunktet er end="\n", der \n står for newline (vi får linjeskift etter teksten som skrives ut). Gjør om programmet du laget til oppgaven ovenfor, slik at teksten skrives ut med tegnet "#" mellom hver bokstav

def hashtagNyBokstavPerLinje():
    inta = input("Skriv en setning: ")
    letter = [x for x in inta]

    for i in letter:
        print(i)
        print("#")

'''
hashtagNyBokstavPerLinje()
'''


# 5 Lag en løkke som skriver ut teksten: "Denne løkka har gjentatt seg n ganger". Her er n et tall som forteller hvor mange ganger løkka har kjørt.

def hvorMangeGangerKjørt():
    for i in range(1,100):
        print(f"Denne løkken har kjørt {i} ganger")

'''
hvorMangeGangerKjørt()
'''