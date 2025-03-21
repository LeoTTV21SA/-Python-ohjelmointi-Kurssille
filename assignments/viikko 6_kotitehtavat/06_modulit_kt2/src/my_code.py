"""

KT2

Tee luokka Tilaus, jolla on kolme jäsenmuuttujaa: tilausnumero, tuotekoodi ja maara.

Toteuta lisäksi funktiot hae_tilaukset, talleta_tilaukset sekä tulosta_tilaukset. Käytä tiedostonnimenä globaalin muuttujan filename arvoa. Käytä talletukseen JSON-formaattia.

Pääohjelma on valmiina, älä muokkaa sitä. Alla esimerkki ohjelman ajosta:


Lisataanko tilaustuote (k/e): k
Tilausnumero: a329847
Tuotekoodi: 22323
Maara: 283
Lisataanko tilaustuote (k/e): k
Tilausnumero: 383838b
Tuotekoodi: 234
Maara: 11
Lisataanko tilaustuote (k/e): e
{'tilausnumero': 'a329847', 'tuotekoodi': '22323', 'maara': 283}
{'tilausnumero': '383838b', 'tuotekoodi': '234', 'maara': 11}

"""

import json

filename="./tilaukset.json"

#Replace pass-lines with your code

class Tilaus:
    def __init__(self, tilausnumero, tuotekoodi, maara):
        self.tilausnumero = tilausnumero
        self.tuotekoodi = tuotekoodi
        self.maara = maara

    def to_dict(self):
        return {
            "tilausnumero": self.tilausnumero,
            "tuotekoodi": self.tuotekoodi,
            "maara": self.maara
        }

def hae_tilaukset():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def talleta_tilaukset(tilaukset):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tilaukset, file, ensure_ascii=False, indent=4)

def tulosta_tilaukset(tilaukset):
    for tilaus in tilaukset:
        print(tilaus)

if __name__ == '__main__':
    tilaukset = hae_tilaukset()

    while True:
        vast = input("Lisataanko tilaustuote (k/e): ")
        if vast.lower() != "k":
            break
        tilausnumero = input("Tilausnumero: ")
        tuotekoodi = input("Tuotekoodi: ")
        maara = int(input("Maara: "))
        tilaus = Tilaus(tilausnumero, tuotekoodi, maara)
        tilaukset.append(tilaus.to_dict())

    talleta_tilaukset(tilaukset)
    del tilaukset

    #Read JSON structure
    t_list=hae_tilaukset()
    #Print JSON structure
    tulosta_tilaukset(t_list)
