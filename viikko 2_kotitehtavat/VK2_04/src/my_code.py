# -*- coding: utf-8 -*-
"""
KT4
Laita vakioon ARVATTAVA_LUKU jonka arvo on 124
Määritä vakio funktion avulla.

Tee ohjelma, joka pyytää arvaamaan lukua.
Jos käyttäjä syötti isomman luvun kuin muuttujassa, niin tulosta : ”Annoit liian suuren luvun”.
Jos taas käyttäjän syöttämä luku oli pienempi kuin vakion luku niin tulosta : ”Annoit liian pienen luvun”.



Kun käyttäjä arvaa luvun oikein niin tulosta : ”Oikein, arvasit luvun 27 kerralla!”.
Missä siis arvo 27 kertoo montako kierrosta meni ennen kuin käyttäjä arvasi oikein

"""

# Määrittele ARVATAVA_LUKU-vakio
def ARVATTAVA_LUKU():
    return 124

# Alusta muuttujat
ARVATTAVA_LUKU = ARVATTAVA_LUKU()
kierrokset = 0  # Yrityslaskuri

# Silmukka, jotta käyttäjä yrittää arvata numeron
while True:
    arvaus = int(input("Arvaa luku: "))  # Lue käyttäjän syöte
    kierrokset += 1  # Kasvata yrityslaskuria

   # Vertaa käyttäjän syötettä kohdenumeroon
    if arvaus > ARVATTAVA_LUKU:
        print("Annoit liian suuren luvun")
    elif arvaus < ARVATTAVA_LUKU:
        print("Annoit liian pienen luvun")
    else:
        # Jos käyttäjä arvaa oikein
        print(f"Oikein, arvasit luvun {kierrokset} kerralla!")
        break  # Poistu silmukasta
