# 4 Funksjonen print() har en parameter som heter end. I utangspunktet er end="\n", der \n står for newline (vi får linjeskift etter teksten som skrives ut). Gjør om programmet du laget til oppgaven ovenfor, slik at teksten skrives ut med tegnet "#" mellom hver bokstav



def hashtagNyBokstavPerLinje():
    inta = input("Skriv en setning: ")
    letter = [x for x in inta]

    for i in letter:
        print(i)
        print("#")



hashtagNyBokstavPerLinje()