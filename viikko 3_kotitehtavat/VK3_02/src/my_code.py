# -*- coding: utf-8 -*-

#
# KT2
#
# Kysy käyttäjältä, montako lukua arvotaan.Jos käyttäjä syöttää arvon < 1, tulostuu "Virhe!"
# Tee lista ja arvo siihen em määrä lukuja  väliltä 0-20.
# Vain parilliset luvut sallitaan.
# Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
# Tulosta luvuista suurin ja pienein samalle riville
# Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna
# Huomaa, että viimeisen luvun jälkeen ei tule pilkkua
#
# Esimerkkiajo ohessa
#
# Montako lukua arvotaan: 3
# Suurin: 6 ja pienin: 0
# 4,0,6
#


import random

def main():
    try:
        maara = int(input("Montako lukua arvotaan: "))
        if maara < 1:
            print("Virhe!")
            return
        
        luvut = []
        while len(luvut) < maara:
            luku = random.randint(0, 20)
            if luku % 2 == 0:
                luvut.append(luku)
        
        print(f"Suurin: {max(luvut)} ja pienin: {min(luvut)}")
        print(",".join(map(str, luvut)))
    
    except ValueError:
        print("Virhe!")

if __name__ == "__main__":
    main()
