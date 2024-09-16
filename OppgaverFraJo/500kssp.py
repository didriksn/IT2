import random

def main():
    list = ["stein", "saks", "papir"]

    stein = 0
    saks = 0
    papir = 0


    for i in range(500000):
        valg = random.choice(list)

        if valg == "stein":
            stein += 1
        elif valg == "saks":
            saks += 1
        else:
            papir += 1


    total = stein + saks + papir

    steinProsent = (stein / total) * 100
    saksProsent = (saks / total) * 100
    papirProsent = (papir / total) * 100
    
    print(f"Papir: {papir}, Prosent: {papirProsent}%")
    print(f"Saks: {saks}, Prosent: {saksProsent}%")
    print(f"Stein: {stein}, Prosent: {steinProsent}%")


main()