# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 06:31:16 2021

@author: Asus
"""

def buscar_elementos_iguales_seguidos(numeros:list)->tuple:
    respuesta=-1
    if len(numeros)==1:
        respuesta=-1
    else:
        for m in range(0,len(numeros)):
            if numeros[m-1]==numeros[m]:
                respuesta=(m-1,m)
    return respuesta
print(buscar_elementos_iguales_seguidos([]))

def contar_apariciones(numeros1:list,numeros2:int)->int:
    r=(len(numeros1))//(len(numeros2))
    l=len(numeros2)
    x=numeros1
    y=numeros2
    c=0
    for n in range(1,r+1):
        if x[(l+1)*(n-1):(l+1)*(n-1)+l]==y:
            c+=1
    return c

#texto ingresado solo con letras mínusculas
def pig_latin(texto:str)->str:
    texto=texto.split(' ',len(texto))
    lista=[]
    for n in texto:
        if n[0]=='a' or n[0]=='e' or n[0]=='i' or n[0]=='o' or n[0]=='u':
            lista.append(palabra_iniciada_vocal(n))
        else:
            lista.append(palabra_iniciada_consonante(n))        
    palabra=lista
    palabra=' '.join(palabra)
    return palabra


def palabra_iniciada_vocal(palabra:str)->str:
    palabra=list(palabra)
    palabra.append('way')
    palabra=''.join(palabra)
    return palabra
def palabra_iniciada_consonante(palabra:str)->str:
    l=len(palabra)
    palabra=list(palabra)
    c=0
    d=0
    while c<l-1:
        if palabra[c]!='a' and palabra[c]!='e' and palabra[c]!='i' and palabra[c]!='o' and palabra[c]!='u':
            d=c
            palabra.append(palabra[c]) 
        else:
            c=l
        c+=1 
    del(palabra[0:d+1])
    palabra.append('ay')
    palabra=''.join(palabra)
    return palabra
#Valores separados por espacios key=value
def str_dic(frase:str)->dict:
    d = dict(x.split("=") for x in frase.split(" "))  
    return d


    

            
            
    

        
        