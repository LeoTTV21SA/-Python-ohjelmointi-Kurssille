# -*- coding: utf-8 -*-

"""

KT5

Esittele muuttuja pii, jolle annat alkuarvoksi piin likiarvon 6 desimaalin tarkkuudella.
Lue käyttäjältä ympyrän halkaisija ja tulosta ympyrän piiri ja pinta-ala kahden desimaalin tarkkuudella

Malli ohessa:

Anna ympyrän halkaisija: 12
Piiri on 37.70
Pinta-ala on 113.10

"""
""

pii = 3.141592

halkaisija = float(input("Anna ympyrän halkaisija: "))
ympyran_piiri = pii * halkaisija
ympyran_pinta_ala = pii * (halkaisija / 2) ** 2

print(f"Piiri on {ympyran_piiri:.2f}")
print(f"Pinta-ala on {ympyran_pinta_ala:.2f}")

if 3.141592 <= pii <= 3.141594:
    print("pii oikein")
print(f"pii={pii:.5f}")
