# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:28:07 2021

@author: Asus
"""

import laboratorio_3 as m

def ejecutar_buscar_elementos_iguales_seguidos()->None:
    lista=input('Ingrese la lista(elementos separados por espacio y sin colchetes)(No colocar espacio y primer elemento, si no el elemento de una vez):')
    listareal=lista.split(' ',len(lista))
    resultado=m.buscar_elementos_iguales_seguidos(listareal)
    if resultado==-1:
        print('No existen elementos iguales seguidos')
    
    else:
        print('Las posiciones de los primeros elementos seguidos son',resultado)
    
    
def ejecutar_contar_apariciones()->None:
   lista=input('Ingrese la lista(elementos separados por espacio y sin colchetes)(No colocar espacio y primer elemento, si no el elemento de una vez):')
   listareal=lista.split(' ',len(lista))
   sublista=input('Ingrese la sublista(elementos separados por espacio y sin colchetes)(No colocar espacio y primer elemento, si no el elemento de una vez):')
   sublistareal=sublista.split(' ',len(lista))
   resultado=m.contar_apariciones(listareal,sublistareal)
   print('El número de apariciones de la sublista en la lista es ',resultado)

def ejecutar_pig_latin()->None:
    frase=str(input('Ingrese la frase:'))
    resultado=m.pig_latin(frase)
    print('La traducción es ',resultado)

def mostrar_menu()->None:
    c=0
    while c==0:
         print('-----------------------')
         print('-----------------------')
         print ("Menu principal")
         print('(1) Retorna las posiciones de los ultimos elementos repetidos en una lista')
         print ('(2) Cuenta el numero de veces que está una sublista en otra lista(Cuenta como uno aquellas sublistas que no se encuentran seguidas de una vez por otra, ej: [1] esta 2 veces en [1,1,1,1])')
         print ("(3) Traducir al pig latin")
         print ('(4) Cerrar apliación')
         respuesta=input('Seleccione una opcion:')
         x=respuesta
         if x=='1':
             ejecutar_buscar_elementos_iguales_seguidos()
         elif x=='2':
             ejecutar_contar_apariciones()
         elif x=='3':
             ejecutar_pig_latin()
         elif x=='4':
             c+=1
         else:
            print('Ingrese una opción valida')
            c=0
mostrar_menu()