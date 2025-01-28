# -*- coding: utf-8 -*-

"""
KT7

Toimeentulotukea maksetaan turvaamaan perustuslaissa tarkoitettu välttämätön toimeentuloa.
Tee ohjelma, joka laskee yksinäisen henkilön tai perheen saaman toimeentulotuen.
Ohjelma laskee tuen määrän käyttäjän syöttämälle määrälle päiviä ja tulostaa toimeentulotuen kokonaismäärän kahdella desimaalilla.
Ohjelma kysyy tuen laskemisessa tarvittavat tiedot yhdessä asumisesta ja lapsista.
Toimeentulotuen määrä lasketaan alla olevan taulukon mukaisesti kahden desimaalin tarkkuudella.
Toimeentulotuen laskemista voidaan toistaa niin monta kertaa kuin ohjelman käyttäjä haluaa. Alla on suuntaa antava esimerkki ohjelman toiminnasta.

Tuki lasketaan siis yhdelle henkilölle, ei esim avioparille


Tuen saaja

Euroa / päivä

Yksin asuva

16,18

Yksinhuoltaja

17,80

Avio- ja avopuolisot kumpikin

13,76

Jokainen 10-17-vuotias lapsi

11,33

Jokainen alle 10-vuotias lapsi

10,20



Tämä ohjelma laskee toimeentulotuen määrän. Alla esimerkkiajo ohjelmasta.

Koodin rakenteelle ei aseteta vaatimuksia muuten kuin, että syötteet annetaan esimerkin mukaisessa järjestyksessä ja ohjelma laskee (tulostaa) tuen määrän oikein. Esimerkkiajosta käy ilmi. että kysymyksiä luupataan eli ohjelma päättyy vasta kun  käyttäjä ei halua enää laskea toimeentulotukea uusilla tiedoilla.



Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): k

Asutko yksin (1) vai puolison kanssa (2) : 1

Onko sinulla/teillä alaikäisiä lapsia (k/e) : k

Kuinka monta alle 10-vuotiasta lasta : 1

Kuinka monta 10-17-vuotiasta lasta : 2

Kuinka monelle päivälle tuki lasketaan : 10



Saat toimeentulotukea 506.60 euroa

Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): e

"""
while True:
    halua = input("Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ").strip().lower()
    if halua != 'k':
        break

    asuminen = input("Asutko yksin (1) vai puolison kanssa (2) : ").strip()
    lapset = input("Onko sinulla/teillä alaikäisiä lapsia (k/e) : ").strip().lower()

    alle_10 = 0
    yli_10 = 0

    if lapset == 'k':
        alle_10 = int(input("Kuinka monta alle 10-vuotiasta lasta : "))
        yli_10 = int(input("Kuinka monta 10-17-vuotiasta lasta : "))

    paivat = int(input("Kuinka monelle päivälle tuki lasketaan : "))

    # Päivärahan laskenta
    if asuminen == '1':
        if lapset == 'k':
            perus = 17.80
        else:
            perus = 16.18
    else:  # asuminen == '2'
        perus = 13.76

    lapsiraha = (alle_10 * 10.20) + (yli_10 * 11.33)
    kokonais = (perus + lapsiraha) * paivat

    print(f"Saat toimeentulotukea {kokonais:.2f} euroa\n")