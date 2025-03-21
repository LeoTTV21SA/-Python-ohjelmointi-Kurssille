"""
KT3

Tutustu omatoimisesti NymPy-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa. Esimerkkisovellus on vapaavalintainen.



"""
#imports here
import numpy as np  # Tuodaan NumPy-kirjasto käyttöön
#Main code here
if __name__ == '__main__':
    # Luodaan 3x3 matriisi (2D-taulukko) NumPy:n avulla
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Alkuperäinen matriisi:")
    print(matrix)

    # Lasketaan matriisin determinantin arvo
    determinant = np.linalg.det(matrix)
    print("Matriisin determinantti:", determinant)
    if np.isclose(determinant, 0):
        print("Huomaa: Matriisi on singulaarinen, mikä voi aiheuttaa ongelmia tietyissä laskuissa.")

    # Lasketaan matriisin transpoosi (rivit ja sarakkeet vaihtavat paikkaa)
    transposed = matrix.T
    print("Matriisin transpoosi:")
    print(transposed)

    # Luodaan 3x3 nollamatriisi
    zero_matrix = np.zeros((3, 3))
    print("3x3 nollamatriisi:")
    print(zero_matrix)

    # Luodaan satunnaislukumatriisi 3x3 (arvot välillä 0-1)
    np.random.seed(42)  # Asetetaan satunnaissiemen toistettavuuden varmistamiseksi
    random_matrix = np.random.rand(3, 3)
    print("Satunnaismatriisi:")
    print(random_matrix)


