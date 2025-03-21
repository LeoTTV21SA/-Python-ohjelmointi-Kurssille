"""
KT4

Tutustu omatoimisesti Pandas-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa.  Esimerkkisovellus on vapaavalintainen.


"""
#imports here
import pandas as pd  # Tuodaan Pandas-kirjasto käyttöön
   #Main code here
if __name__ == '__main__':
    # Luodaan esimerkkidataa DataFrame-muodossa
    data = {
        "Nimi": ["Anna", "Matti", "Liisa", "Pekka"],
        "Ikä": [25, 30, 22, 28],
        "Kaupunki": ["Helsinki", "Tampere", "Turku", "Oulu"]
    }
    df = pd.DataFrame(data)  # Muutetaan sanakirja DataFrameksi
    
    # Tulostetaan DataFrame
    print("Alkuperäinen DataFrame:")
    print(df)
    
    # Tallennetaan DataFrame CSV-tiedostoon
    df.to_csv("data.csv", index=False)
    print("Data tallennettu CSV-tiedostoon 'data.csv'")
    
    # Luetaan CSV-tiedosto takaisin DataFrameksi
    df_luettu = pd.read_csv("data.csv")
    print("CSV-tiedostosta luettu DataFrame:")
    print(df_luettu)
    
    # Suodatetaan DataFrame, jossa vain yli 25-vuotiaat henkilöt
    filtered_df = df[df["Ikä"] > 25]
    print("Yli 25-vuotiaat henkilöt:")
    print(filtered_df)

