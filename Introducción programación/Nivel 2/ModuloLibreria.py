# -*- coding: utf-8 -*-
def crear_libro(nom: str, cod: str,autor: int, adp: int, cant: int, pdv: float, cpu: float)->dict:
    dic_libro = { "nombre": nom, 
                       "codigo": cod,  
                       "autor": autor, 
                       "añoPublicacion": adp,
                       "cantidad": cant,
                       "precio": pdv, 
                       "costoProduccion": cpu}
    return dic_libro

#PROGRAMA PRINCIPAL
libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200 , 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100 , 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien",1937, 50 , 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20 , 26000, 13000)

def mayor_ganancia(libro1:dict,libro2:dict,libro3:dict,libro4:dict)->dict:
    ganancia_1=libro1['precio']-libro1['costoProduccion']
    ganancia_2=libro2['precio']-libro2['costoProduccion']
    ganancia_3=libro3['precio']-libro3['costoProduccion']
    ganancia_4=libro4['precio']-libro4['costoProduccion']
    mayor=max(ganancia_1,ganancia_2,ganancia_3,ganancia_4)
    if mayor==ganancia_1:
        a=libro1
    elif mayor==ganancia_2:
        a=libro2
    elif mayor==ganancia_3:
        a=libro3
    elif mayor==ganancia_4:
        a=libro4
    return a

def hacer_pedido(libro1:dict,libro2:dict,libro3:dict,libro4:dict,nombre_libro:str)->bool:
    if nombre_libro==libro1['nombre']:
        if libro1['cantidad']<=50:
            a=True
        else:
            a=False
    elif nombre_libro==libro2['nombre']:
        if libro2['cantidad']<=50:
            a=True
        else:
            a=False
    elif nombre_libro==libro3['nombre']:
        if libro3['cantidad']<=50:
            a=True
        else:
            a=False
    elif nombre_libro==libro4['nombre']:
        if libro4['cantidad']<=50:
            a=True
        else:
            a=False
    return a

def publicacion_antes_anio(libro1:dict,libro2:dict,libro3:dict,libro4:dict,anio:int)->dict:
    a='publicado después del año ingresado'
    b=a
    c=a
    d=a
    if libro1['añoPublicacion']<anio:
        a=libro1['nombre']
    if libro2['añoPublicacion']<anio:
        b=libro1['nombre']
    if libro1['añoPublicacion']<anio:
        c=libro1['nombre']
    if libro1['añoPublicacion']<anio:
        d=libro1['nombre']
    return a,b,c,d

def ganacias_venta_libro(libro1:dict,libro2:dict,libro3:dict,libro4:dict,nombre_libro:str,cantidad_ventas:int)->dict:
    a=libro1['precio']-libro1['costoProduccion']
    b=libro2['precio']-libro2['costoProduccion']
    c=libro3['precio']-libro3['costoProduccion']
    d=libro4['precio']-libro4['costoProduccion']
    x=0
    if nombre_libro==libro1['nombre']:
        x=a*cantidad_ventas
    
    elif nombre_libro==libro2['nombre']:
        x=b*cantidad_ventas
    
    elif nombre_libro==libro3['nombre']:
        x=c*cantidad_ventas
    
    elif nombre_libro==libro4['nombre']:
        x=d*cantidad_ventas
    return x
def venta_por_mayor(libro1:dict,libro2:dict,libro3:dict,libro4:dict,nombre_libro:str,cantidad_ventas:int)->dict:
    des=0
    costo='No valido para venta por mayor'
    if nombre_libro==libro1['nombre']:
        if 0.25*libro1['cantidad']<cantidad_ventas<0.5*libro1['cantidad']:
            des=0.1
        elif 0.5*libro1['cantidad']<cantidad_ventas<0.75*libro1['cantidad']:
            des=0.2
        elif 0.75*libro1['cantidad']<cantidad_ventas<=libro1['cantidad']:
            des=0.3
        
    elif nombre_libro==libro2['nombre']:
        if 0.25*libro2['cantidad']<cantidad_ventas<0.5*libro2['cantidad']:
            des=0.1
        elif 0.5*libro2['cantidad']<cantidad_ventas<0.75*libro2['cantidad']:
            des=0.2
        elif 0.75*libro2['cantidad']<cantidad_ventas<=libro2['cantidad']:
            des=0.3
            
    elif nombre_libro==libro3['nombre']:
        if 0.25*libro3['cantidad']<cantidad_ventas<0.5*libro3['cantidad']:
            des=0.1
        elif 0.5*libro3['cantidad']<cantidad_ventas<0.75*libro3['cantidad']:
            des=0.2
        elif 0.75*libro3['cantidad']<cantidad_ventas<=libro3['cantidad']:
            des=0.3
   
    elif nombre_libro==libro4['nombre']:
        if 0.25*libro4['cantidad']<cantidad_ventas<0.5*libro4['cantidad']:
            des=0.1
        elif 0.5*libro4['cantidad']<cantidad_ventas<0.75*libro4['cantidad']:
            des=0.2
        elif 0.75*libro4['cantidad']<cantidad_ventas<=libro4['cantidad']:
            des=0.3
    if nombre_libro==libro1['nombre']:
        costo=libro1['precio']*(1-des)*cantidad_ventas
    elif nombre_libro==libro1['nombre']:
        costo=libro1['precio']*(1-des)*cantidad_ventas
    elif nombre_libro==libro1['nombre']:
        costo=libro1['precio']*(1-des)*cantidad_ventas
    return des,costo
    
        
        
        
    
        
        