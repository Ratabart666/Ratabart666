# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:08:52 2022

@author: Asus
"""
import Algoritmosnumericos as Alg
import pandas as pd

print('Bienvenido equipo de ingenieros y cientificos, espero ser de utilidad')
print('')
print('')


def calificacion(nom1, nom2):
    datos1 = pd.read_csv(nom1)
    print('El archivo cargado de caracteristicas numericas es:')
    print('')
    print(datos1.to_markdown())
    pesos = [datos1.iloc[0].tolist()]
    datos1 = datos1[1:]
    datos2 = open(nom2, 'r')
    content_datos2 = datos2.read()
    print(100*'-')
    print('El archivo cargado de características cualitativas es:')
    print('')
    print(content_datos2)
    resultados = {}
    for i in range(len(datos1)):
        resultados[i] = Alg.producto(
            [datos1.iloc[i].tolist()], pesos) * 100*(1/10)
    print('El resultado por orden es:')
    for i in resultados:
        print(100*'-')
        print('')
        print(i, ' : ', round(resultados[i]), '%')
    print('')
    return ('Ha finalizado.')


def menu():
    print('Nota 1: verifique como se organizan los archivo en el archivo formato.tx')
    print('')
    print('Nota 2: Digite - en cualquier input si quiere salir')
    print(' ')
    x = input('Ingrese el nombre del archivo de caracteristicas numericas txt(El archivo debe estar en la misma carpeta que este script):')
    y = input('Ingrese el nombre del archivo de caracteristicas cualitativas txt(El archivo debe estar en la misma carpeta que este script):')
    if x != '-' and y != '-':
        print(100*'#')
        calificacion(x, y)
        print(100*'#')
        menu()
    else:
        print('Hasta luego ingenieros y cientificos, gracias por utilizar el programa')


menu()
