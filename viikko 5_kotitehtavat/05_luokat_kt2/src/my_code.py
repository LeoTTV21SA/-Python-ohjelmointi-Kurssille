"""
KT2


Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa. Ohjelmalla (pääohjelmassa) on lista, johon käyttäjä voi lisätä Osake-olioita. Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.


Tee luokka Osake, jolla on jäsenmuuttujat:
- nimi
- ostohinta (>0, osakekohtainen ostohinta)
- maara (> 0, omistettujen osakkeiden lkm)



Osakkeella on metodit:

- tulosta_arvo, jonka parametreina on  kasvuprosentin ja ajanjakson vuosina (tässä järjestyksessä). tulosta_arvo-metodi kutsuu toista Osake-luokan  metodia laske_tuotto_yhdelle_vuodelle, joka laskee vuosikohtaisen tuoton. tulosta_arvo kutsuu laske_tuotto_yhdelle_vuodelle-metodia vuosien lukumäärän verran. Siis, jos lasketaan tuottoa kolmelle vuodelle, niin laske_tuotto_yhdelle_vuodelle kutsutaan kolme kertaa. Huomio "korkoa korolle". Valuutat tulostetaan kahden desimaalin tarkkuudella.

- laske_tuotto_yhdelle_vuodelle -metodi palauttaa tuoton yhdelle vuodelle. Metodi on staattinen ja saa parametrinaan kasvuprosentin ja hinnan vuoden alussa (tässä järjesyksessä).

Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvosta vuosien jälkeen.

Esimerkkiajo:


Anna osakkeen nimi: Nokia
Anna osakkeen ostohinta/kpl: 10
Anna ostettujen osakkeiden lukumäärä: 1000
Lisää osakkeita (k/e)? k

Anna osakkeen nimi: Fortum
Anna osakkeen ostohinta/kpl: 12
Anna ostettujen osakkeiden lukumäärä: 127
Lisää osakkeita (k/e)? e

Anna kasvuprosentti: 5
Anna vuodet: 3

Nokia 1000 10.0
Osakkeen potin arvo on 11576.25 ja tuotto 1576.25

Fortum 127 12.0
Osakkeen potin arvo on 1764.22 ja tuotto 240.22

Koko potin arvo on 13340.47
"""
#Write class and imports here!
    
class Osake:
    def __init__(self, nimi, ostohinta, maara):
        if ostohinta <= 0 or maara <= 0:
            raise ValueError("Ostohinnan ja määrän on oltava suurempia kuin 0.")
        self.nimi = nimi
        self.ostohinta = ostohinta
        self.maara = maara
    
    @staticmethod
    def laske_tuotto_yhdelle_vuodelle(kasvuprosentti, hinta):
        return hinta * (1 + kasvuprosentti / 100)
    
    def tulosta_arvo(self, kasvuprosentti, vuodet):
        nykyinen_arvo = self.ostohinta * self.maara
        for _ in range(vuodet):
            nykyinen_arvo = Osake.laske_tuotto_yhdelle_vuodelle(kasvuprosentti, nykyinen_arvo)
        tuotto = nykyinen_arvo - (self.ostohinta * self.maara)
        print(f"{self.nimi} {self.maara} {self.ostohinta:.2f}")
        print(f"Osakkeen potin arvo on {nykyinen_arvo:.2f} ja tuotto {tuotto:.2f}\n")
        return nykyinen_arvo

if __name__ == "__main__":
    osakkeet = []
    
    while True:
        nimi = input("Anna osakkeen nimi: ")
        ostohinta = float(input("Anna osakkeen ostohinta/kpl: "))
        maara = int(input("Anna ostettujen osakkeiden lukumäärä: "))
        osakkeet.append(Osake(nimi, ostohinta, maara))
        
        jatka = input("Lisää osakkeita (k/e)? ").strip().lower()
        if jatka != 'k':
            break
    
    kasvuprosentti = float(input("Anna kasvuprosentti: "))
    vuodet = int(input("Anna vuodet: "))
    
    koko_potin_arvo = 0
    for osake in osakkeet:
        koko_potin_arvo += osake.tulosta_arvo(kasvuprosentti, vuodet)
    
    print(f"Koko potin arvo on {koko_potin_arvo:.2f}")


