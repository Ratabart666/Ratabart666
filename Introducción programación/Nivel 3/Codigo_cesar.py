# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:24:21 2021

@author: Asus
"""


def descifrar_codigo_cesar(texto_cifrado: str, corrimiento: int)->str:
    numero_caracter=0
    caracter_nuevo=''
    numero_caracter_nuevo=0
    cadena_nueva=''
    sub_sale=''
    
    for caracter in texto_cifrado:
        numero_caracter=ord(caracter)
        if numero_caracter<=122 and numero_caracter>=97+corrimiento:
            numero_caracter_nuevo=numero_caracter-corrimiento
            caracter_nuevo=chr(numero_caracter_nuevo)
            cadena_nueva+=caracter_nuevo
            
        elif numero_caracter>=97 and numero_caracter<97+corrimiento:
            sub_sale=corrimiento-(numero_caracter-96)
            numero_caracter_nuevo=122-sub_sale
            caracter_nuevo=chr(numero_caracter_nuevo)
            cadena_nueva+=caracter_nuevo
        
        elif numero_caracter<=90 and numero_caracter>=65+corrimiento:
            numero_caracter_nuevo=numero_caracter-corrimiento
            caracter_nuevo=chr(numero_caracter_nuevo)
            cadena_nueva+=caracter_nuevo
        
        elif numero_caracter>=65 and numero_caracter<65+corrimiento:
            sub_sale=corrimiento-(numero_caracter-64)
            numero_caracter_nuevo=90-sub_sale
            caracter_nuevo=chr(numero_caracter_nuevo)
            cadena_nueva+=caracter_nuevo
        else:
            cadena_nueva+=caracter
            
            
            
    return cadena_nueva
