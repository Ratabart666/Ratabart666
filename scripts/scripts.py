# -*- coding: utf-8 -*-
"""
Created on Sun May  8 04:13:14 2022

@author: Asus
"""
from os import listdir
import os


def correr(extensiones, ruta):
    for i in listdir(ruta):
        for j in extensiones:
            if j != '.ipynb':
                if i[-len(j):] == j:
                    try:
                        print('Inicio archivo')
                        print(i)
                        print('#')
                        print((open(ruta+'/'+i).read()))
                        exec(open(ruta+'/'+i).read())
                        print('Final archivo')
                    except:
                        print('Inicio')
                        print(i)
                        print('#')
                        print('No se pudo leer el archivo anterior')
                        print('Final archivo')

            else:
                if i[-len(j):] == j:
                    try:
                        print('Inicio archivo')
                        print(i)
                        print('#')
                        print((open(ruta+'/'+i).read()))
                        print('Final archivo')
                    except:
                        print('Inicio archivo')
                        print(i)
                        print('#')
                        print('No se pudo leer el archivo anterior')
                        print('Final archivo')


def corrercarpetas(extensiones, ruta):
    for i in listdir(ruta):
        print('Inicio carpeta')
        print(i)
        correr(extensiones, ruta+'/'+i)
        print('Final carpeta')


def directorios(nombre, ruta, cantidad):
    os.chdir(ruta)
    for i in range(int(cantidad)):
        print(i)
        os.mkdir(str(nombre)+str(i+1))


def menu() -> None:
    print('Elija un script:')
    print('1- Correr (Corre los archivos de una carpeta)')
    print('2- Directorios (varios directorios en una ruta)')
    print('3- Correr carpetas(correr carpetas con carpetas que contienen archivos)')
    print('#- Terminar programa')
    x = input('Ingrese la opción:')
    aux = None
    aux2 = None
    aux3 = None
    if x == '1':
        aux = input('Ingrese las extensiones a leer:').split(',')
        aux2 = str(input('Ingrese la ruta:'))
        correr(aux, aux2)
        menu()

    elif x == '2':
        aux = input('Ingrese nombre común directorios:')
        aux2 = input('Ingrese la ruta donde se crean los directorios:')
        aux3 = input('Ingrese la cantidad de directorios:')
        directorios(aux, aux2, aux3)
        menu()
    elif x == '3':
        aux = input('Ingrese las extensiones a leer:').split(',')
        aux2 = input('Ingrese la ruta donde estan las carpetas:')
        corrercarpetas(aux, aux2)
        menu()

    elif x == '#':
        print('Terminó el programa')


menu()
