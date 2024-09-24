# Importerer random biblioteket
import random

# Definerer informasjon om landene ved hjelp av dictionary
# infoOmLand = {
#     "Norge": ["Oslo", 5500000, ["Sverige", "Finland", "Russland"]],
#     "Sverige": ["Stockholm", 10500000, ["Norge", "Finland"]],
#     "Canada": ["Ottawa", 39000000, ["USA"]],
#     "Malaysia": ["Kuala Lumpur", 34000000, ["Indonesia", "Brunei", "Singapore", "Thailand"]]
# }


spørsmålOgSvar = {
    "Hva er hovedstaden i Norge": "oslo",
    "Hvor mange innbyggere er det i Norge": "5500000",
    "Hvor mange naboland har Norge": "3",
    "Hva er hovedstaden i Sverige": "stockholm",
    "Hvor mange innbyggere er det i Sverige": "10500000",
    "Hvor mange naboland har Sverige": "2",
    "Hva er hovedstaden i Canada": "ottawa",
    "Hvor mange innbyggere er det i Canada": "39000000",
    "Hvor mange naboland har Canada": "1",
    "Hva er hovedstaden i Malaysia": "kuala Lumpur",
    "Hvor mange innbyggere er det i Malaysia": "34000000",
    "Hvor mange naboland har Malaysia": "4",
}


# Definerer funksjonen "quiz"
def quiz():
    # Holder telling på antall riktige svar
    antallRiktige = 0

    # De ulike landene
    land = ["Norge", "Sverige", "Canada", "Malaysia"]

    # Hver variabel velger et tilfeldig land fra listen og putter det som sin verdi
    randomland1 = land[random.randint(0,3)]
    randomland2 = land[random.randint(0,3)]
    randomland3 = land[random.randint(0,3)]

    # Stiller det første spørsmålet
    sprsm1 = input(f"Hva er hovedstaden i {randomland1}: ").lower()

    # Sjekker om det er riktig eller feil, i forhold til svarene i "spørsmålOgSvar" dictionary-en
    if sprsm1 == spørsmålOgSvar[f"Hva er hovedstaden i {randomland1}"]:
        antallRiktige += 1
        print("Riktig!")
    else: 
        print("Feil!")

    # Stiller det andre spørsmålet
    sprsm2 = input(f"Hvor mange innbyggere er det i {randomland2}: ").lower()

    # Sjekker om det er riktig eller feil, i forhold til svarene i "spørsmålOgSvar" dictionary-en
    if sprsm2 == spørsmålOgSvar[f"Hvor mange innbyggere er det i {randomland2}"]:
        antallRiktige += 1
        print("Riktig!")
    else: 
        print("Feil!")



    # Stiller det tredje spørsmålet
    sprsm3 = input(f"Hvor mange naboland har {randomland3}: ").lower()

    # Sjekker om det er riktig eller feil, i forhold til svarene i "spørsmålOgSvar" dictionary-en
    if sprsm3 == spørsmålOgSvar[f"Hvor mange naboland har {randomland3}"]:
        antallRiktige += 1
        print("Riktig!")
    else: 
        print("Feil!")

    
    if antallRiktige == 0:
        print(f"Du fikk {antallRiktige} av 3 riktige svar. Skuffende.")
    elif antallRiktige == 1:
        print(f"Du fikk {antallRiktige} av 3 riktige svar. Mindre bra.")
    elif antallRiktige == 2:
        print(f"Du fikk {antallRiktige} av 3 riktige svar. Bra!")
    elif antallRiktige == 3:
        print(f"Du fikk {antallRiktige} av 3 riktige svar. Kjempebra!")


# Kaller funksjonen "quiz"
quiz() 