"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU. 

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

"""

#Write functions here!

def LuoNimetJaArvosanat():
    arvosanat = {}
    while True:
        nimi = input("Anna nimi (LOPPU lopettaa): ")
        if nimi == "LOPPU":
            break
        if nimi in arvosanat:
            print("Nimi on jo lisätty. Anna eri nimi.")
            continue
        try:
            arvosana = int(input("Anna arvosana (0-5): "))
            if arvosana < 0:
                arvosana = 0
            elif arvosana > 5:
                arvosana = 5
            arvosanat[nimi] = arvosana
        except ValueError:
            print("Virheellinen syöte! Anna kokonaisluku.")
    return arvosanat

def TulostaHylatyt(arvosanat):
    hylatyt = [nimi for nimi, arvosana in arvosanat.items() if arvosana == 0]
    if hylatyt:
        print("Hylätyt:", ", ".join(hylatyt))

def PalautaHylattyjenMaara(arvosanat):
    maara = sum(1 for arvosana in arvosanat.values() if arvosana == 0)
    print(maara)
    return maara

def TulostaKaikki(arvosanat):
    for nimi, arvosana in arvosanat.items():
        print(nimi, arvosana)

if __name__ == "__main__":
     #Write main program below this line
    arvosanat = LuoNimetJaArvosanat()
    if PalautaHylattyjenMaara(arvosanat) > 0:
        TulostaHylatyt(arvosanat)
    else:
        TulostaKaikki(arvosanat)

