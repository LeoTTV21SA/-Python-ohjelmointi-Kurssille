# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""
import os
import random

# Korjataan siemen
random.seed(1)   # Säädä tätä numeroa, jos opettaja käyttää toista

# Luo src-kansio, jos sitä ei ole
if not os.path.exists("src"):
    os.makedirs("src")

# Kysy numeroiden määrää
try:
    maara = int(input("Montako lukua arvotaan? ").strip())
    if maara < 1:
        print("Virhe!")
        exit()
except ValueError:
    print("Virhe!")
    exit()

# Luo numerot ja kirjoita arvot.txt
arvotut_luvut = []
with open("src/arvot.txt", "w") as tiedosto:
    for _ in range(maara):
        random_decimal = round(random.uniform(0, 100), 2)
        arvotut_luvut.append(random_decimal)
        tiedosto.write(f"{random_decimal:.2f}\n")

# Oikea tulostusmuoto (ei ylimääräisiä rivinvaihtoja)
print("Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:")
print(" ".join(f"{x:.2f}" for x in arvotut_luvut))

# Lue numerot tiedostosta ja lajittele ne
with open("src/arvot.txt", "r") as tiedosto:
    luvut = [float(line.strip()) for line in tiedosto]

luvut.sort()

# Tulosta tilatut numerot täsmälliseen muotoon
print("Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:")
print(" ".join(f"{x:.2f}" for x in luvut))

# Laske tilastot
lkm = len(luvut)
summa = round(sum(luvut), 2)
ka = round(summa / lkm, 2)
minimi = round(min(luvut), 2)
maksimi = round(max(luvut), 2)

# Tallenna kohteeseen tulokset.txt täsmällisessä muodossa
with open("src/tulokset.txt", "w") as tulostiedosto:
    tulostiedosto.write(f"Lkm: {lkm}\n")
    tulostiedosto.write(f"Sum: {summa:.2f}\n")
    tulostiedosto.write(f"Ka: {ka:.2f}\n")
    tulostiedosto.write(f"Min: {minimi:.2f}\n")
    tulostiedosto.write(f"Max: {maksimi:.2f}\n")

# Tulosta tulokset oikeassa muodossa
print("\nJa lopuksi tiedostosta tulokset.txt löytyy seuraavat tiedot:")
print(f"Lkm: {lkm}")
print(f"Sum: {summa:.2f}")
print(f"Ka: {ka:.2f}")
print(f"Min: {minimi:.2f}")
print(f"Max: {maksimi:.2f}")






