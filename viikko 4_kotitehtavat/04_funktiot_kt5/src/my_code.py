"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU. Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022. Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt. Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
#Write functions, define global variables, and import modules here!

from datetime import datetime

def LueAutot():
    autot = {}
    while True:
        rekisterinumero = input("Syötä auton rekisterinumero (LOPPU lopettaa): ")
        if rekisterinumero.upper() == "LOPPU":
            break
        
        while True:
            paivamaara = input("Syötä rekisteröintipäivämäärä (dd.mm.yyyy): ")
            try:
                paivamaara_obj = datetime.strptime(paivamaara, "%d.%m.%Y")
                break  # Kelvollinen päivämäärä, jatketaan eteenpäin
            except ValueError:
                print("Virheellinen päivämäärä. Yritä uudelleen.")
        
        autot[rekisterinumero] = paivamaara_obj
    
    return autot

def TalletaTiedostoon(autot, tiedostonimi="autot.txt"):
    with open(tiedostonimi, "w") as tiedosto:
        for rekisterinumero, paivamaara in autot.items():
            tiedosto.write(f"{rekisterinumero}\t{paivamaara.strftime('%d.%m.%Y')}\n")

def LueTiedostosta(tiedostonimi="autot.txt"):
    autot = {}
    try:
        with open(tiedostonimi, "r") as tiedosto:
            for line in tiedosto:
                line = line.strip()
                if line:
                    rekisterinumero, paivamaara = line.split("\t")
                    autot[rekisterinumero] = datetime.strptime(paivamaara, "%d.%m.%Y")
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt. Palautetaan tyhjä sanakirja.")
    return autot

def TulostaTiedot(autot):
    if not autot:
        print("Ei rekisteröintitietoja.")
    else:
        for rekisterinumero, paivamaara in autot.items():
            print(f"{rekisterinumero}: {paivamaara.strftime('%d.%m.%Y')}")

if __name__ == "__main__":
    autot = LueAutot()
    TalletaTiedostoon(autot)
    luetut_autot = LueTiedostosta()
    TulostaTiedot(luetut_autot)



    


