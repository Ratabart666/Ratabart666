# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:39:09 2022

@author: Asus
"""

def algoritmo_euclides(x:int,y:int)->int:
    '''Ingresados 2 numeros (x,y) retorna iterativamente a traves del algoritmo de euclides el maximo comun divisor'''
    a=max(x,y)
    b=min(x,y)
    #El proceso iterativo es encontrar un entero e y un natural r, tal que 0=<r<e
    #Estos enteros deben satisfacer que a=b*e+r
    r=a%b#residuo
    if r!=0:
        #Si el residuo no es cero se continua el proceso iterativo
        return algoritmo_euclides(b,r)
    else:
        #cuando el residuo es cero se retorna b, que sería el MCD de (x,y)
        return b
    
    
def menu():
    print(100*'#')
    print('Ingrese una opción: ')
    print('')
    print('1) Algoritmo de euclides')
    print('#) Salir')
    x=input('Ingrese la opción deseada: ')
    if x=='1':
        print(100*'-')
        m=int(input('Primer número para el algoritmo de euclides: '))
        n=int(input('Segundo número para el algoritmo de euclides: '))
        print(algoritmo_euclides(m,n))
        menu()
    if x=='#':
        print(100*'-')
        print('Gracias por usar la aplicación')
    else:
        menu()
menu()
