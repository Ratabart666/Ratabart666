# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 07:47:01 2021

@author: Asus
"""

import calculadoracondicionales as mod

def ejecutar_bisiesto()->None:
    anio=int(input('Ingrese el año:'))
    resultado=mod.bisiesto(anio)
    print(resultado)
    
def ejecutar_clasificar()->None:
   a1=float(input('Ángulo 1:'))
   a2=float(input('Ángulo 2:'))
   a3=float(input('Ángulo 3:'))
   resultado=mod.clasificar(a1,a2,a3)
   print(resultado)

def ejecutar_solucionar()->None:
    a=float(input('a:'))
    b=float(input('b:'))
    c=float(input('c:'))
    resultado=mod.solucionar(a,b,c)
    print(resultado)

def mostrar_menu()->str:
    c=0
    while c==0:
         print ("Menu principal")
         print ("(1) Año bisiesto")
         print ("(2) Tipo de triángulo")
         print ("(3) Solución ecuación cuadrática")
         print ('(4) Cerrar apliación')
         respuesta=input('Seleccione una opcion:')
         x=respuesta
         if x=='1':
             (ejecutar_bisiesto())
         elif x=='2':
             (ejecutar_clasificar())
         elif x=='3':
             (ejecutar_solucionar())
         elif x=='4':
             c+=1
         else:
            c=0
            
        
        
                           
        
def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()
iniciar_aplicacion()
