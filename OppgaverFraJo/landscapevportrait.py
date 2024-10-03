def pororland(høyde, bredde):
    if (høyde > bredde):
        return "Bildet ditt er portrait"
    elif (bredde > høyde):
        return "Bildet ditt er landscape"
    else:
        return "Bildet ditt er kvadratisk eller ikke et ordentlig bilde"


print(pororland(int(input("Skriv høyden på bildet ditt i pixels: ")), int(input("Skriv bredden på bildet ditt i pixels: "))))