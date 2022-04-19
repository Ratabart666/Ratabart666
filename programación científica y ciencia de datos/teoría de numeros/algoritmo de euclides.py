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
    print(str(a)+str('=')+str(b)+str('*')+str(a//b)+str('+')+str(r))
    if r!=0:
        #Si el residuo no es cero se continua el proceso iterativo
        return algoritmo_euclides(b,r)
    else:
        #cuando el residuo es cero se retorna b, que sería el MCD de (x,y)
        return b

