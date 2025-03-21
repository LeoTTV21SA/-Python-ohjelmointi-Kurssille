# -*- coding: utf-8 -*-

"""
KT 5

Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

"""
# Kysy käyttäjältä nimeä
nimi = input("Anna nimesi: ").strip()

# Vahvista, että nimi on enintään 18 merkkiä
if len(nimi) > 18:
    print("Virhe!")
    exit()

# Hanki nimen pituus
pituus = len(nimi)

# Laske maksimitila kohdistuksen oikealle
max_spaces = (pituus - 1) * 2 # Jokainen kirjain siirtää kahta tilaa

# Luettelo tiedoston rivien tallentamisesta
lines = []

# Tulosta tuloste laskevassa järjestyksessä (viimeisestä kirjaimesta ensimmäiseen)
for i in range(pituus):
    spaces = " " * (max_spaces - (i * 2))  # Alkutilat
    print(spaces + nimi[-(i + 1)])   # Otamme kirjaimet päinvastaisessa järjestyksessä
    lines.append(spaces + nimi[-(i + 1)])

# Tallenna tiedostoon nimi.txt
with open("src/nimi.txt", "w") as tiedosto:  # Tallenna kohteeseen 'src/nimi.txt', koska testi etsii sitä sieltä
    for line in lines:
        tiedosto.write(line + "\n")  # Kirjoita tiedoston jokainen rivi

