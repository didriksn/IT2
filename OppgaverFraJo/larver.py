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
            print("Det funket ikke. Kanskje du ikke skrev et numerisk tall. Pass på at du skriver tallene direkte, og ikke med bokstaver.")


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