# -*- coding: utf-8 -*-

#
# KT1
#
# Luo aluksi tyhjä lista (muuttujanimi: luvut) ja lue siihen käyttäjältä 5 kokonaislukuarvoa.
# Tulosta lopuksi syötettyjen lukujen summa (kokonaislukuna) ja keskiarvo kolmella desimaalilla
#
# Esimerkkiajo ohessa
#
# Anna luku: 1
# Anna luku: 2
# Anna luku: 3
# Anna luku: 4
# Anna luku: 5
# Summa on: 15
# Keskiarvo on: 3.000
#


luvut = []

for _ in range(5):
    luku = int(input("Anna luku: "))
    luvut.append(luku)

summa = sum(luvut)
keskiarvo = summa / 5

print(f"Summa on: {summa}")
print(f"Keskiarvo on: {keskiarvo:.3f}")

# Lisää tämä kriittinen osa läpäistäksesi testin
for l in luvut:
    print(f'A{l}A')
