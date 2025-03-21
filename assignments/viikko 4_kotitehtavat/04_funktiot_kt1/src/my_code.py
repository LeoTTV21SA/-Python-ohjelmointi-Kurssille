"""
KT1


Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 

Funktio palauttaa kokonaislukuarvon seuraavasti:

 

1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.

-1, jos syötetty luku on negatiivinen. 

 

Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.


”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

"""

#Write KysyJaTestaaLuku function here!
def KysyJaTestaaLuku():
    while True:
        try:
            luku = int(input("Syötä kokonaisluku: "))
            return 1 if luku > 0 else 0 if luku == 0 else -1
        except ValueError:
            print("Virheellinen syöte, anna kokonaisluku.")


if __name__ == "__main__":
    #Write main program below this line
  tulokset = {1: "Luku oli positiivinen", 0: "Luku oli nolla", -1: "Luku oli negatiivinen"}
  print(tulokset[KysyJaTestaaLuku()])

