# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 07:50:37 2021

@author: Asus
"""
import lab_2 as m

def ejecutar_es_palindroma()->None:
    frase=input('Ingrese la frase:')
    resultado=m.es_palindroma(frase)
    print(resultado)
    
def ejecutar_letra_mas_comun()->None:
   frase=input('Ingrese la frase:')
   resultado=m.letra_mas_comun(frase)
   print(resultado)

def ejecutar_invertir_cadena()->None:
    frase=input('Ingrese la frase:')
    resultado=m.invertir_cadena(frase)
    print(resultado)

def mostrar_menu()->str:
    c=0
    while c==0:
         print('-----------------------')
         print('-----------------------')
         print ("Menu principal")
         print ("(1) Frases palíndroma")
         print ("(2) Letra más comun")
         print ("(3) Cadena Invertida")
         print ('(4) Cerrar apliación')
         respuesta=input('Seleccione una opcion:')
         x=respuesta
         if x=='1':
             ejecutar_es_palindroma()
         elif x=='2':
             ejecutar_letra_mas_comun()
         elif x=='3':
             ejecutar_invertir_cadena()
         elif x=='4':
             c+=1
         else:
            print('Ingrese una opción valida')
            c=0
mostrar_menu()
            