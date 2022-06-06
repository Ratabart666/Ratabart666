def tiempo_transferencia(tamano:float,ancho_banda:int)-> str:
    horas=((512/225)*(tamano/ancho_banda))//1
    minutos=(((((512/225)*(tamano/ancho_banda)-horas)*60)))//1
    segundos=round(((((512/225)*(tamano/ancho_banda)-horas)*60)-minutos)*60)
    return 'El archivo tardará '+str(horas)+' horas, '+str(minutos)+' minutos y  '+str(segundos)+' segundos en transferirse'

def costo_procesamiento_compromiso(Dedicados_compromiso:int,Compartidos_compromiso:int,Costo:float)->float:
    Costo_mes_compromiso=round(720*((Costo*Dedicados_compromiso)**(9/10)+((9/10)*Costo*Compartidos_compromiso)**(17/20)),2)
    return(Costo_mes_compromiso)
   
def costo_procesamiento_libre(Dedicados_libre:int,Compartidos_libre:int,Costo:float)->float:
    costo_mes_libre=round(720*(Costo*Dedicados_libre+(9/10)*Costo*Compartidos_libre),2)
    return(costo_mes_libre)

def costo_almacenamiento(Lectura:int,Escritura:int,Almacenamiento:float)->float:
    costo_mes_almacenamiento=round(Almacenamiento*(0.023)+Lectura*(0.004/1000)+Escritura*(0.005/1000),2)
    return(costo_mes_almacenamiento)

def costo_transferencia(datos:float,porcentaje_aws:float)->float:
    costo_mes_transferencia=round(((1-porcentaje_aws)*datos-1)*(0.09)+porcentaje_aws*datos*0.02,2)
    return(costo_mes_transferencia)

import math
def costo_total(servidores_compromiso:int,porcentaje_compartidas_compromiso:float,servidores_libres:int,porcentaje_compartidas_libres:float,costo_dedicado:float,solicitudes_totales:int,almacenamiento:float,datos:float,porcentaje_aws:float)->str:
   
    Dedicados_compromiso=math.floor((servidores_compromiso*(1-porcentaje_compartidas_compromiso)))
    Compartidos_compromiso=math.ceil((servidores_compromiso*porcentaje_compartidas_compromiso))
   
    Costo_mes_compromiso=720*((costo_dedicado*Dedicados_compromiso)**(9/10)+((9/10)*costo_dedicado*Compartidos_compromiso)**(17/20))
   
    Dedicados_libre=math.floor((servidores_libres*(1-porcentaje_compartidas_libres)))
    Compartidos_libre=math.ceil((servidores_libres*porcentaje_compartidas_libres))
  
    Costo_mes_libre=720*(costo_dedicado*Dedicados_libre+(9/10)*costo_dedicado*Compartidos_libre)
    
    Lectura=math.ceil((solicitudes_totales*(2/3)))
    Escritura=math.floor((solicitudes_totales*(1/3)))
    
    costo_mes_almacenamiento=almacenamiento*(0.023)+Lectura*(0.004/1000)+Escritura*(0.005/1000)
    
    costo_mes_transferencia=((1-porcentaje_aws)*datos-1)*(0.09)+porcentaje_aws*datos*0.02
    
    costo_mensual=round(Costo_mes_compromiso+Costo_mes_libre+costo_mes_almacenamiento+costo_mes_transferencia,2)
    return(str('El costo total mensual de mantener la infraestructura en AWS es $'+str(costo_mensual)+' USD.'))

