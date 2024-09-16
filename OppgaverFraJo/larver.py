import random

print("Vi skal forske litt på larver og vi trenger din hjelp \n")

larveLengder = []

for i in range(96):
    larveLengder.append(random.randint(1, 15))

def inputs(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except (ValueError, EOFError, MemoryError):
            print("bro du skrev IKKE et tall liksom bro hvordan failer du i å skrive et tall liksom det er det letteste tingen noensinne liksom wtf hva skjer hvordan failer du en slik enkel task bro jeg er dypt skuffet må jeg ærlig si men jaja synd for deg du får bare kjøre koden på nytt du fortjener det uansett for å ikke ha skrevet et tall engang når det var nøyaktig det som var bedt av deg")


inp1 = inputs("Du har 4 larver, hvor lang (i cm) er den første?: ")
inp2 = inputs("Den andre: ")
inp3 = inputs("Den tredje: ")
inp4 = inputs("Og til slutt den fjerde: ")

larveLengder.append(inp1)
larveLengder.append(inp2)
larveLengder.append(inp3)
larveLengder.append(inp4)


størsteLarve = max(larveLengder)
minsteLarve = min(larveLengder)
gjennomsnittStørrelse = sum(larveLengder) / len(larveLengder)

print(f"\nDen største larven er {størsteLarve} lang!")
print(f"\nDen minste larven er {minsteLarve} lang!")
print(f"\nDen gjennomsnittlige lengden på larvene er {gjennomsnittStørrelse}")