import random


def inputs(prompt):
    while True:
        try:
            return int(input(prompt))
        except (ValueError, EOFError, MemoryError, KeyboardInterrupt):
            print("Det funket ikke. Kanskje du ikke skrev et numerisk tall.")

def strInputs(prompt):
    while True:
        try:
            return input(prompt)
        except (ValueError, EOFError, MemoryError, KeyboardInterrupt):
            print("\nInvalid navn, synd for deg.")


def skryting(navn, mengder):
    komplementer = ["snill", "morsom", "omtenksom", "smart", "følsom", "sjenerøs", "troverdig", "glad", "elskeverdig", "kul"]
    nyKomplementer = []


    for i in range(0, mengder):
        randomTall = random.randint(0, len(komplementer) - 1)
        nyKomplementer.append(komplementer[randomTall])
        komplementer.remove(komplementer[randomTall])



    if mengder != 1:
        print(f"Kjære {navn}! Du er {", ".join(nyKomplementer[:-1])} og {"".join(nyKomplementer[-1])}")
    else:
        print(f"Kjære {navn}! Du er {"".join(nyKomplementer)}")



navn = strInputs("Hva er da ditt navn?: ")
print(f"Hei {navn}, du skal få noen komplement: ")
mengder = inputs("Hvor mange komplement vil du ha (minst 1, maks 10): ")

if (mengder >= 1 and mengder <= 10):
    skryting(navn, mengder)
else: 
    print("Det gikk ikke helt, prøv å skriv inn ett numerisk integer som er innenfor definert rekkevidde.")