# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 07:54:33 2021

@author: Asus
"""

from math import pi

radio = float(input("Digite el radio del círculo: "))

#Menú de opciones
print("Seleccione una opción: ")
print("a) Calcular diámetro: ")
print("b) Calcular perímetro: ")
print("c) Calcular el área: ")
print("d) Salir del programa")

opcion = input("Digite a, b, c o d y pulse enter: ")

while opcion != "d":
    if opcion == "a":
        diametro = 2 * radio
        print("El diámetro es: ", diametro)
        opcion = input("Digite a, b, c o d y pulse enter: ")
    elif opcion == "b":
        perimetro = 2  *pi * radio
        print("El perímetro es: ", perimetro)
        opcion = input("Digite a, b, c o d y pulse enter: ")
    elif opcion == "c":
        area = 2 * pi * radio ** 2
        print("El área es: ",area)
        opcion = input("Digite a, b, c o d y pulse enter: ") 
    else:
        print("Por favor seleccione una opción válida")
        opcion = input("Digite a, b, c o d y pulse enter: ")
        
print("Gracias por utilizar la calculadora")