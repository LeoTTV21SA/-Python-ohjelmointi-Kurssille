# -*- coding: utf-8 -*-

"""
KT1
Lue käyttäjältä kaksi lukua ja tulosta niistä suurempi. Käytä if-else -lausetta vertailussa.

"""
luku1 = float(input("Anna esimäinen liku: "))
luku2 = float(input("Anna toinen luku: "))

if luku1 > luku2:
    print(f"Suurempi liku on: {luku1}")
else:
    print(f"Suurempi luku on: {luku2}")