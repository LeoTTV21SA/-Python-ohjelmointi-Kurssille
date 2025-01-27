# -*- coding: utf-8 -*-

"""
KT2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:

 Hyvä (jos arvosana oli 9 tai 10)

 Kelpo (jos 7 - 8)

 Tyydyttävä (jos 5 - 6)

 Heikko (jos 4)

 Toteuta ohjelma if-elif-else -rakenteella.

 Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

 
"""

# Leer el número del usuario
arvosana = int(input("Anna koenumero (4-10 väliltä): "))

# Verificar si la nota está dentro del rango válido
if arvosana < 4 or arvosana > 10:
    print("Et antanut arvosanaa annetulta väliltä")
else:
    # Clasificar según la calificación
    if arvosana == 9 or arvosana == 10:
        print("Hyvä")
    elif arvosana == 7 or arvosana == 8:
        print("Kelpo")
    elif arvosana == 5 or arvosana == 6:
        print("Tyydyttävä")
    elif arvosana == 4:
        print("Heikko")


