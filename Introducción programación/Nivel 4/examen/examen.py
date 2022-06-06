import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


    
def grafica_req_1(icfes:pd.DataFrame)->None:
    nacionalidad=icfes.groupby('ESTRATO').ESTRATO.count().div(len(icfes))
    plt.figure()
    nacionalidad.plot(kind='bar',xlabel='Estrato',ylabel='Frecuencia',title='Distribución nacionalidades')
    plt.show()
    #completar la función  
    
def grafica_req_2(icfes:pd.DataFrame)->None:
    plt.figure()
    generoestrato=icfes.groupby('GENERO').GENERO.count() 
    generoestrato.plot(kind='pie',ylabel='Estudiantes',title='Diagrama de torta de la distribución de género en Colombia ',autopct='%1.1f%%',shadow=True)
    plt.legend(loc='upper right')
    plt.show()
    #completar la función
    
    
def grafica_req_3(icfes:pd.DataFrame)->None:
    plt.figure()
    icfes.boxplot(column = 'PUNT_GLOBAL', by = 'DEPARTAMENTO', rot = (90), figsize = (15,10))
    plt.xlabel('Departamento')
    plt.show()
        
    
    return 'Gracias por utilizar la aplicación,ingrese una opción:'
    
        

    #completar la función
    
    plt.show()
def estudianteslectura(matriz:list,lectura:str)->str:#10
    '''Retorna el número de estudiantes con un hábito de lectura dado(30 minutos o menos,Entre 30 y 60 minutos,Entre 1 y 2 horas,Mas de 2 horas,No leo por entretenimiento ).
    Parámetros: 
        matriz: Matriz con la información de estrato vs lectura.
        lectura: Hábito de lectura que se desea analizar.
    Retorno:
        Número de estudiantes con el hábito de lectura dado.'''
    
    total=0
    respuesta=0
    if lectura=='30 minutos o menos':
        for fila in matriz:
            total+=fila[0]
    elif lectura=='Entre 30 y 60 minutos':
        for fila in matriz:
            total+=fila[1]
    elif lectura=='Entre 1 y 2 horas':
        for fila in matriz:
            total+=fila[2]
    elif lectura=='Más de 2 horas':
        for fila in matriz:
            total+=fila[3]
    elif lectura=='No leo por entretenimiento':
        for fila in matriz:
            total+=fila[4]
    if total!=0:
        respuesta=total
    return respuesta
    
def funcion_req_4(datos_matriz:tuple)->int:
    total=estudianteslectura(datos_matriz[0],'30 minutos o menos')+estudianteslectura(datos_matriz[0],'Entre 30 y 60 minutos')
    return total

def funcion_req_5(datos_matriz:tuple)->int:
    lista=[]
    for estrato in datos_matriz[0]:
        lista.append(estrato[4])
    total=max(lista)
    for estrato in range(0,6):
        if lista[estrato]==total:
            respuesta=estrato+1
        
        
    return respuesta
    
def iniciarAplicacion()->None:
    icfes = cargar_datos("ICFES.csv")
    grafica_req_1(icfes)
    grafica_req_2(icfes)
    grafica_req_3(icfes)
    
    matriz = cargar_matriz(icfes)
    print("RESULTADO REQ 4: ", funcion_req_4(matriz))
    print("RESULTADO REQ 5: ", funcion_req_5(matriz))

    
def cargar_datos(nombreArchivo: str)->pd.DataFrame:
        icfes = pd.read_csv(nombreArchivo)
        return icfes

def cargar_matriz(datos: pd.DataFrame)->tuple:
    estratos = datos["ESTRATO"].unique()
    estratos.sort()
    estratos_diccionario = dict(list(enumerate(estratos)))
    estratos_dict = dict(list(enumerate(estratos)))
    lectura = datos["LECTURA_DIARIA"].unique()
    lectura.sort()
    aux = lectura[2]
    lectura[2] = lectura[1]
    lectura[1] = aux
    lectura_diccionario = dict(list(enumerate(lectura)))
    lectura_dict = dict(list(enumerate(lectura)))
    
    matrix = []
    
    for index in estratos_dict:
        stratum = estratos_dict[index]
        estratos_dict[index] = set(datos.index[datos['ESTRATO'] == stratum].tolist())
     
    
    for index in lectura_dict:
        reading_hours = lectura_dict[index]
        lectura_dict[index] = datos.index[datos['LECTURA_DIARIA'] == reading_hours].tolist()

    for index_1 in estratos_dict:
        stratum_set = estratos_dict[index_1]
        row = []
        
        for index_2 in lectura_dict:
           reading_hours_set = lectura_dict[index_2]
           value_position = len(stratum_set.intersection(reading_hours_set))
           row.append(value_position)
         
        final_row = tuple(row)
        matrix.append(final_row)
     
    final_matrix =  (matrix, estratos_diccionario, lectura_diccionario)  
    
    return final_matrix
    
     
iniciarAplicacion()
