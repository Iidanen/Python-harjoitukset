luku = input("Anna luku: ")

if luku != "":
    pienin = float(luku)
    suurin = float(luku)

    while luku != "":
        luku = input("Anna luku: ")

        if luku != "":
            luku = float(luku)

            if luku < pienin:
                pienin = luku

            if luku > suurin:
                suurin = luku

    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)