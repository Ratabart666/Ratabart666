# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 07:54:10 2021

@author: Asus
"""
def es_palindroma(frase:str)->bool:
    a=False
    cadena=frase.lower()
    cadena=cadena.replace(' ','')
    cadena=cadena.replace('á','a')
    cadena=cadena.replace('é','e')
    cadena=cadena.replace('í','i')
    cadena=cadena.replace('ó','o')
    cadena=cadena.replace('ú','u')
    cadena2=cadena[::-1]  
    if cadena==cadena2:
        a=True
    return a
def letra_mas_comun(frase:str)->str:
    cadena=frase.lower()
    cadena=cadena.replace(' ','')
    cadena=cadena.replace('á','a')
    cadena=cadena.replace('é','e')
    cadena=cadena.replace('í','i')
    cadena=cadena.replace('ó','o')
    cadena=cadena.replace('ú','u')
    cadena=cadena.replace('ú','u')
    cadena=cadena.replace(',','')
    cadena=cadena.replace('.','')
    mayor=0
    respuesta=''
    for x in frase:
        y=cadena.count(x)      
        if y>mayor:
            mayor=y
            respuesta=x
    return respuesta

def invertir_cadena(frase:str)->str:
    cadena2=frase[::-1]
    return cadena2
    
    
        
      
            
                  
    

        

            
            
        
    
    
    


