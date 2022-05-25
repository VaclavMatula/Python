rok = int(input("Zadejte cislo: "))
if rok % 4 == 0:
    if rok % 100 != 0:
        print ("prestupny rok")
    elif rok % 400 == 0:
        print ("prestupny rok")
    else:
        print ("neprestupny rok")
else:
    print ("neprestupny rok")