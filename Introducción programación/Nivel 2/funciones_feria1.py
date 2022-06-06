# -*- coding: utf-8 -*-
import math as math
import random as rand

def buscar_bolita(posicion_inicial: int, posicion_apuesta: int)->bool:
    vaso1= False
    vaso2= False
    vaso3= False
    
    if posicion_inicial==1: 
        vaso1=True
    elif posicion_inicial==2:
        vaso2=True
    else:
        vaso3=True
        
    x= rand.randint(1,3)
    if x==1:
        y=vaso1
        vaso1=vaso2
        vaso2=y
    elif x==2: 
        y=vaso2
        vaso2=vaso3
        vaso3=y
    else:
        y=vaso3
        vaso3=vaso1
        vaso1=y
    x= rand.randint(1,3)
  
    if x==1:
        y=vaso1
        vaso1=vaso2
        vaso2=y
    elif x==2: 
        y=vaso2
        vaso2=vaso3
        vaso3=y
    else:
        y=vaso3
        vaso3=vaso1
        vaso1=y
    
    x=rand.randint(1,3)
    if x==1:
        y=vaso1
        vaso1=vaso2
        vaso2=y
    elif x== 2: 
        y= vaso2
        vaso2=vaso3
        vaso3=y
    else:
        y=vaso3
        vaso3=vaso1
        vaso1=y
        
    respuesta = False
    if posicion_apuesta == 1 and vaso1==True:
        respuesta = True
    elif posicion_apuesta == 2 and vaso2==True:
        respuesta = True
    elif posicion_apuesta == 3 and vaso3==True:
        respuesta = True
    return respuesta

def tiro_al_blanco(velocidad_inicial:float,angulo_alfa:float,angulo_beta:float)->float:
    v=(velocidad_inicial/3.6)*rand.uniform(0.9,1.1)
    alfa_grados=angulo_alfa+rand.uniform(-0.5,0.5)
    alfa=math.radians(alfa_grados)
    beta_grados=angulo_beta+rand.uniform(-0.5,0.5)
    beta=math.radians(beta_grados)
    seno_2_alfa=math.sin(2*alfa)
    coseno_beta=math.cos(beta)
    d=(v**2)*(seno_2_alfa)*(1/9.8)
    z=round(((d**2)-(14*d*coseno_beta)+49)**(1/2),1)
    
    if 0<=z<0.1:
        a=50
    elif 0.1<=z<0.2:
        a=20
    elif 0.2<=z<0.3:
        a=10
    elif 0.3<=z<=0.4:
        a=5
    else:
        a=0
    return a
def coordenadas_respecto_centro_mesa(velocidad_inicial:float,angulo_alfa:float,angulo_beta:float)->float:
    v=(velocidad_inicial/3.6)*rand.uniform(0.9,1.1)
    alfa_grados=angulo_alfa+rand.uniform(-0.5,0.5)
    alfa=math.radians(alfa_grados)
    beta_grados=angulo_beta+rand.uniform(-0.5,0.5)
    beta=math.radians(beta_grados)
    seno_2_alfa=math.sin(2*alfa)
    coseno_beta=math.cos(beta)
    d=(v**2)*(seno_2_alfa)*(1/9.8)
    z=round(((d**2)-(14*d*coseno_beta)+49)**(1/2),2)
    return z




        
    
    

    




