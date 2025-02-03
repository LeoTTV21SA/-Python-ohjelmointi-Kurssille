"""
KT1

Luontojärjestö KuopionBongarit tarvitsee uuden rekisterin, johon kaikki lintuhavainnot rekisteröidään.

Tee julkinen luokka Havainto, jolla on ominaisuudet:
- lintulaji, teksti
- maara, kokonaisluku, jos <0 muutetaan nollaksi
- tyyppi, teksti (Eli oliko lintu esim paikallinen vai muuttava)
- havaintopvm, datetime, ei voi olla tulevaisuuteen
- paikka, teksti
- kuvaus, teksti
 
Tee luokalle muodostin, jossa annetaan arvot kaikille luokan attribuuteille yllä olevassa järjestyksessä.
Tee kaikille jäsenmuuttujille getterit ja setterit Python-tekniikalla,  jotta tietoja pääsee muokkaamaan ja lukemaan. Tulosta getterissä viesti "getter" ja vastaavasti setterissä viesti "setter".
Tee myös __str__-metodi.  
Testaa pääohjelmassa. Mitään sen kummempaa käyttöliittymää ei tarvitse tehdä. Riittää, että luot yhden Havainto olion ja tulostat sen tiedot hyödyntäen __str__ metodia.

"""
#Write class and imports here!

from datetime import datetime

class Havainto:
    def __init__(self, lintulaji, maara, tyyppi, havaintopvm, paikka, kuvaus):
        self.lintulaji = lintulaji
        self.maara = maara
        self.tyyppi = tyyppi
        self.havaintopvm = havaintopvm
        self.paikka = paikka
        self.kuvaus = kuvaus

    @property
    def lintulaji(self):
        print("getter")
        return self._lintulaji

    @lintulaji.setter
    def lintulaji(self, value):
        print("setter")
        self._lintulaji = value

    @property
    def maara(self):
        print("getter")
        return self._maara

    @maara.setter
    def maara(self, value):
        print("setter")
        self._maara = max(0, value)

    @property
    def tyyppi(self):
        print("getter")
        return self._tyyppi

    @tyyppi.setter
    def tyyppi(self, value):
        print("setter")
        self._tyyppi = value

    @property
    def havaintopvm(self):
        print("getter")
        return self._havaintopvm

    @havaintopvm.setter
    def havaintopvm(self, value):
        print("setter")
        if value > datetime.now():
            raise ValueError("Havaintopäivämäärä ei voi olla tulevaisuudessa.")
        self._havaintopvm = value

    @property
    def paikka(self):
        print("getter")
        return self._paikka

    @paikka.setter
    def paikka(self, value):
        print("setter")
        self._paikka = value

    @property
    def kuvaus(self):
        print("getter")
        return self._kuvaus

    @kuvaus.setter
    def kuvaus(self, value):
        print("setter")
        self._kuvaus = value

    def __str__(self):
        return f"Lintulaji: {self.lintulaji}, Määrä: {self.maara}, Tyyppi: {self.tyyppi}, Päivämäärä: {self.havaintopvm.strftime('%d.%m.%Y')}, Paikka: {self.paikka}, Kuvaus: {self.kuvaus}"


if __name__ == "__main__":
    havainto = Havainto("Varis", 3, "Paikallinen", datetime(2023, 5, 15), "Kuopio", "Nähtiin puistossa")
    print(havainto)


