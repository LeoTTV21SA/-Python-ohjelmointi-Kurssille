# -*- coding: utf-8 -*-
"""

KT4

Lue nimi, pituus ja paino em nimisiin muuttujiin. Käytä juuri noita muuttujanimiä.
Esittele lisäksi bmi muuttuja ja alusta se nollaksi. Kysy käyttäjältä nimi, pituus metreinä ja paino kiloina.
Laske painoindeksi bmi muuttujaan seuraavasti:


bmi = paino / pituus ^ 2



Tulosta lopuksi:


Jussi Juonio pituutesi on 1.81 m ja painosi 104.0 kg
Painoindeksisi on siten 31.75

Huomaa, että bmi tulee kahdella desimaalilla

"""
nimi = "??"
paino = 0.0
pituus = 0.0
bmi = 0.0

nimi = input("Anna Kokonimi: ")
pituus = float(input("Anna Pituus m: "))
paino = float(input("Anna Paino kg: "))

bmi = paino / (pituus ** 2)

print(f"{nimi} pituutesi on {pituus:.2f} m ja painosi {paino:.1f} kg")
print(f"Painoindeksisi on siten {bmi:.2f}")



