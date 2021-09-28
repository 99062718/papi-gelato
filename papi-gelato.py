def stap1():
    smaakjesLijst = []
    try:
        bolletjes = int(input("Hoeveel bolletjes wilt u?\n"))
        if bolletjes >= 1 and bolletjes <= 3:
            for x in range(1, bolletjes+1):
                smaak = smaakjes(x)
                smaakjesLijst.append(smaak)
            stap2(str(bolletjes))
        elif bolletjes >= 4 and bolletjes <= 8:
            print("Dan krijgt u van mij een bakje met " + str(bolletjes) + " bolletjes")
            for x in range(1, bolletjes+1):
                smaak = smaakjes(x)
                smaakjesLijst.append(smaak)
        else:
            print("Sorry, zulke grote bakken hebben we niet")
            stap1()
    except:
        print("Sorry dat snap ik niet...")
        stap1()

def smaakjes(bolletjeNummer):
    smaak = input("Welke smaak wilt u voor bolletje nummer " + str(bolletjeNummer) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?\n").lower()
    if smaak == "a":
        return "aardbei"
    elif smaak == "c":
        return "chocolade"
    elif smaak == "m":
        return "munt"
    elif smaak == "v":
        return "vanille"
    else:
        print("Sorry dat snap ik niet...")
        smaakjes(bolletjeNummer)

def stap2(bolletjes):
    hoorntjeOfBakje = input("Wilt u deze " + bolletjes + " bolletje(s) in A) een hoorntje of B) een bakje?\n").lower()
    if hoorntjeOfBakje != "hoorntje" and hoorntjeOfBakje != "bakje":
        print("Sorry dat snap ik niet...")
        stap2(bolletjes)
    else:
        stap3(bolletjes, hoorntjeOfBakje)

def stap3(bolletjes, hoorntjeOfBakje):
    choice = input("Hier is uw " + hoorntjeOfBakje + " met " + bolletjes + " bolletje(s). Wilt u nog meer bestellen? (Y/N)\n").lower()
    if choice != "y" and choice != "n":
        print("Sorry dat snap ik niet...")
        stap3(bolletjes, hoorntjeOfBakje)
    else:
        stap1() if choice == "y" else print("Bedankt en tot ziens!")

print("Welkom bij Papi Gelato")

stap1()