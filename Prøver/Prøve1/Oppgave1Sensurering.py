# Definerer de problematiske ordene slik at de er dynamisk
# Sjekker også for andre som inneholder "fis" som referer til det dårlige ordet "fis"
problematiskeOrd = ["fis", "fiser", "fisen", "fisene", "fiste", "fisens", "bæsj", "tiss", "banan", "kvantefysikk"]

# Lager funksjonen som sensurer fullt
def fullSensurering(ord):
    # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    individuelleBokstaver = [i for i in ord]

    # Går gjennom hver bokstav i ordet for å endre det
    for i in range(0, len(individuelleBokstaver)):
        # Endrer hver bokstav til "#", fordi det er ganske vanlig å sensurere med det
        individuelleBokstaver[i] = "#"

    return "".join(individuelleBokstaver)


# Lager en dictionary for å sensurere de dårlige ordene
sensur = {}

# Keysene i dictionary-en er basert på ordene i problematiskeOrd listen
for i in problematiskeOrd:
    sensur[problematiskeOrd[i]] = fullSensurering(problematiskeOrd[i])



# Lager funksjonen
def sensurer(setning, problematiskeOrd, sensur):
    # Seperer hvert ord i setningen hver for seg
    setning = setning.split()

    for i in range(0, len(setning) - 1):
        # Sjekker om alle bokstavene i ordet er stort, fordi hvis det er det er det mulig at vi snakker om ski-organisasjonen. Om alle bokstavene ikke er stor kjører vi videre
        if setning[i] != setning[i].upper():
            # Sammenligner ord i setningen med hvert av de problematiske ordene
            for j in range(0, len(problematiskeOrd)):
                if setning[i].lower() == problematiskeOrd[j].lower():
                    setning[i] = sensur[setning[i]]

    print(" ".join(setning))




sensurer("Den som fisen først er var, den er fisens rette far", problematiskeOrd, sensur)
sensurer("FIS globally governs skiing and snowboarding and oversees over 7000 events annually in Alpine, Cross-Country, Ski Jumping, Nordic Combined and many more.", problematiskeOrd, sensur)
sensurer("Fiskal blir benyttet om det som har med statskassen eller regnskap å gjøre, som for eksempel «fiskale avgifter» (statlige avgifter), eller «det fiskale året 2005» (regnskapsåret 2005). Fiskale skatter og avgifter har til formål å skaffe inntekter til staten.", problematiskeOrd, sensur)
sensurer("Oppskrifter med fisk og sjømat for alle, til middag, lunsj og fest. Lær om behandling av fisk og sjømat.", problematiskeOrd, sensur)