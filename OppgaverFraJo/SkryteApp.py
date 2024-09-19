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




komplementer = ["fantastisk", "klok", "sterk", "omsorgsfull", "morsom", "pålitelig", "dyktig", "vakker", "utholdende", "engasjert", "inspirerende", "modig", "kreativ", "talentfull", "snill", "omtenksom", "ærlig", "fokusert", "optimistisk", "generøs", "sjarmerende", "forståelsesfull", "trofast", "lojal", "dypsindig", "dedikert", "tålmodig", "nytenkende", "ærlighet", "innsiktsfull", "kjærlig", "motiverende", "besluttsom", "energisk", "entusiastisk", "oppmerksom", "selvstendig", "åpen", "respektfull", "hensynsfull", "anerkjennende", "munter", "stilfull", "genuin", "fantasifull", "elegant", "rolig", "barmhjertig", "humoristisk", "artig", "dypsindig", "ressurssterk", "organisert", "rettferdig", "dyrevennlig", "velbalansert", "intelligent", "kunnskapsrik", "oppfinnsom", "beskjeden", "selvsikker", "godhjertet", "karismatisk", "beskyttende", "bevisst", "handlekraftig", "selvkontrollert", "oppløftende", "varm", "glad", "reflektert", "ansvarsfull", "rettskaffen", "artig", "omsorgsbevisst", "medfølende", "lidenskapelig", "ydmyk", "omgjengelig", "karaktersterk", "tolerant", "raskt-tenkende", "flittig", "diplomatisk", "ærlighetssøkende", "sprudlende", "åpenhjertig", "påpasselig", "verdifull", "ubetinget", "godlynt", "lattermild", "forutsigbar", "glødende", "skarp", "tilpasningsdyktig", "veslevoksen", "pålest", "nøyaktig", "fornuftig", "medmenneskelig", "grasiøs", "velvillig", "sjarmerende", "sunn", "søt", "klok", "kunstnerisk", "kraftfull", "kultivert", "kunnskapsrik"]
    

def skryting(navn, mengder):
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
mengder = inputs(f"Hvor mange komplement vil du ha (minst 1, maks {len(komplementer)}): ")

if (mengder >= 1 and mengder <= len(komplementer)):
    skryting(navn, mengder)
else: 
    print("Det gikk ikke helt, prøv å skriv inn ett numerisk integer som er innenfor definert rekkevidde.")