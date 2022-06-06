# -*- coding: utf-8 -*-

import funciones_feria1 as feria

def mostrar_menu()->None:
    print("Opciones")
    print("1.", "Buscar la bolita")
    print("2.", "Tiro al blanco")

def opcion1()->None:
    print("-"*32)
    print("Buscar la bolita")
    print("-"*32)
    posicion_inicial = int(input("Por favor seleccione en cuál vaso debe iniciar la bolita: 1, 2 o 3 "))
    posicion_apuesta = int(input("Por favor seleccione en cuál vaso apuesta que va a quedar la bolita: 1, 2 o 3 "))
    resultado = feria.buscar_bolita(posicion_inicial, posicion_apuesta)
    if resultado==True:
        print("¡Victoria: encontraste la bolita!")
    else:
        print("¡Perdiste!")

def opcion2()->None:
    print("-"*32)
    print("Tiro al blanco")
    print("-"*32)
    print("Recuerde que el blanco se encuentra a 7 metros de distancia y tiene 40 centímetros de diámetro en total")
    velocidad = float(input("¿Con qué velocidad quiere lanzar la bola? (Km/h) "))
    alfa = float(input("¿A qué ángulo quiere enviar la bola con respecto al plano horizontal? "))
    beta = float(input("¿A qué ángulo quiere enviar la bola con respecto al centro de la mesa? "))

    puntos = feria.tiro_al_blanco(velocidad,alfa,beta)
    if puntos!=0:
        print("¡Le atinaste el blanco! Ganaste", puntos, "puntos")
    else:
        print("¡Fallaste!")
        x=feria.coordenadas_respecto_centro_mesa(velocidad,alfa,beta)
        print("Pero con esos valores la bola debería haber caído a",x, "metros de distancia del centro de la mesa")


mostrar_menu()
opcion = int(input("Por favor seleccione una opción del menú: "))

if opcion == 1:
    opcion1()
elif opcion == 2:
    opcion2()
else:
    print("Por favor seleccione una opción válida")
    
