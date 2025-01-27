# -*- coding: utf-8 -*-

"""

KT5

Kysy käyttäjältä kaksi lukua. Ensimmäisessä luvussa annetaan alkuarvo  lukuparille ja toisessa montako kertaa lukuparia kasvatetaan/vähennetään.


Tulosta lukuparit allekkain for-silmukkaa käyttäen. Vasen luku siis kasvaa ja oikea vähenee yhden verran kullakin rivillä.

Jos käyttäjä antaa luvut 10 ja 5, tulostus näyttää seuraavalta:
10,10
11,9
12,8
13,7
14,6
15,5



Eli tulostuvan lukuparin ensimmäinen arvo kasvaa ja toinen vähenee lähtien liikkeelle luvusta 10 toistuen 5 kertaa

"""

def main():
    # Pedir al usuario los dos números
    alkuarvo = int(input("Anna alkuarvo: "))  # Número inicial
    toistot = int(input("Anna toistojen määrä: "))  # Número de repeticiones

    # Usar un bucle for para imprimir los pares de números
    for i in range(toistot + 1):  # Repite 'toistot' veces, incluyendo 0
        vasen = alkuarvo + i  # El número izquierdo incrementa en 1 cada vez
        oikea = alkuarvo - i  # El número derecho disminuye en 1 cada vez
        print(f"{vasen},{oikea}")


if __name__ == "__main__":
    main()

