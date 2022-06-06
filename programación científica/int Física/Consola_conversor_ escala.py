# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:31:38 2021

@author: Asus
"""
import Conversor_escala as mod

def mostrar_menu()->None:
    print("Opciones")
    print("1.", "Calcular diametro en escala")
    print("2.", "Calcular distancia al sol en escala")
    print("3.", "Salir de la apliación")
def opcion1()->None:
    y=int(input('Ingrese el orden de magnitud de el radio en metros:'))
    z=float(input('Ingrese el numero que acompaña al orden de magnitud:'))
    w=mod.diametro_escala(y,z)
    print('La longitud correspondiente del diametro en escala es',str(w),'in')
def opcion2()->None:
    y=int(input('Ingrese el orden de magnitud de la distancia al sol en metros:'))
    z=float(input('Ingrese el numero que acompaña al orden de magnitud:'))
    w=mod.distancia_sol_escala(y,z) 
    print('La longitud correspondiente de la distancia al sol en escala es',str(w),'in')
    
    
mostrar_menu()
opcion = int(input("Por favor seleccione una opción del menú: "))

if opcion == 1:
    opcion1()
elif opcion == 2:
    opcion2()
else:
    print("Por favor seleccione una opción válida")