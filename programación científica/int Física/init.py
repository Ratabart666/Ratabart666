# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:31:38 2021

@author: Asus
"""
def diametro_escala(orden_magnitud: int, numero: float) -> float:
    """Dado el orden de magnitud y un  numero(El orden de magnitud y el numero corresponden al radio de un planeta),
    retorna la distancia en pulgadas(Suponiendo que 1pulg=0.1Mmi), asi convertimos
    distancias del sistema solar a escala humana"""
    x = (2 * numero) * (10**orden_magnitud)
    y = 0.62 * (10**-8)
    z = x * y
    return str(z) + " in"


def distancia_sol_escala(orden_magnitud: int, numero: float) -> float:
    """Dado el orden de magnitud y un  numero(El orden de magnitud y el numero corresponden a la distancia al sol de un planeta),
    retorna la distancia en pulgadas(Suponiendo que 1pulg=0.1Mmi), asi convertimos
    distancias del sistema solar a escala humana"""
    x = (numero) * (10**orden_magnitud)
    y = 0.62 * (10**-8)
    z = x * y
    return str(z) + " in"



def menu():
    print(100*"#")
    print("Elija una opcion:")
    print("1) Dado el radio de un planeta (metros)retorna el diametro en escala( 1in=0.1Mmi)")
    print("2) Dado la distancia al sol (metros) retorna esta distancia en diametro (1in=0.1Mmi")
    print("#) Salir")
    x = input("Elija una opcion: ")
    y = None
    z = None
    try:
        if x == "1":
            y = int(input("Elija el orden de magnitud: "))
            z = float(input("Elija el numero: "))
            print(diametro_escala(y, z))
            print(100*'#')
            menu()
        if x == "2":
            y = int(input("Elija el orden de magnitud: "))
            z = float(input("Elija el numero: "))
            print(distancia_sol_escala(y, z))
            print(100*'#')
            menu()
        if x == "#":
            print("Gracias")
        else:
            print("Ingrese una opcion valida")
    except:
        print('Error, intente de nuevo')
        menu()

menu()
