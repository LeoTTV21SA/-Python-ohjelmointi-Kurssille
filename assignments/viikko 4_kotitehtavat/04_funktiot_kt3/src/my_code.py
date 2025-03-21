"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

 
"""
#Write functions and define global variables here!

# Globaali vakio kriittiselle pisteelle
KR_PISTE = 90.0

def KysyHypynPituus():
    """Kysyy käyttäjältä hypyn pituuden ja palauttaa sen liukulukuna."""
    while True:
        try:
            pituus = float(input("Anna hypyn pituus (0.5 m välein): "))
            if pituus >= 0:
                return pituus
            else:
                print("Pituuden on oltava positiivinen.")
        except ValueError:
            print("Virheellinen syöte. Anna numero.")

def KysyTuomareidenPisteet():
    """Kysyy viiden tuomarin pisteet ja palauttaa ne listana."""
    pisteet = []
    for i in range(5):
        while True:
            try:
                piste = float(input(f"Anna tuomari {i+1}:n pisteet (0-20, 0.5 välein): "))
                if 0 <= piste <= 20 and piste * 2 == int(piste * 2):  # Tarkistaa 0.5 välin
                    pisteet.append(piste)
                    break
                else:
                    print("Virheellinen syöte. Anna piste välillä 0-20, 0.5 välein.")
            except ValueError:
                print("Virheellinen syöte. Anna numero.")
    return pisteet

def LaskeHypynPisteet(pituus, pisteet):
    """Laskee hypyn kokonaispisteet ja palauttaa sen."""
    piste_ero = (pituus - KR_PISTE) * 1.8
    pisteet.sort()
    keskimmäiset_pisteet = sum(pisteet[1:4])  # Kolmen keskimmäisen pisteet
    return piste_ero + keskimmäiset_pisteet + 60

if __name__ == "__main__":
    #Write main program below this line
    hypyn_pituus = KysyHypynPituus()
    tuomari_pisteet = KysyTuomareidenPisteet()
    hypyn_pisteet = LaskeHypynPisteet(hypyn_pituus, tuomari_pisteet)
    
    print(f"Hypyn pituus: {hypyn_pituus} m")
    print(f"Hypyn pisteet: {hypyn_pisteet:.1f}")

