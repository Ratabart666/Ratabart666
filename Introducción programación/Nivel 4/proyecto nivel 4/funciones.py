import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def cargar_datos(nombre:str)->pd.DataFrame:#0
    """
    Crea un nuevo DataFrame a partir del original


    Parámetros: 
        nombr: Nombre del archivo csv.

    Retorno:
        Dataframe con la información del icfes.

    """
    df=pd.read_csv(nombre)
    return df

def nacionalidad(data:pd.DataFrame)->str:#1
    """
    Crea un gráfico de barras el cual contenga la información de frecuencia de todas las nacionalidades
    a excepción de las nacionalidades Colombiana y Venezolana.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.

    Retorno:
        Grafico de barras que contiene las frecuencias de las nacionalidades,excepto Colombiana y Venezolana.

    """
    nacionalidad=data[(data.NACIONALIDAD!='COLOMBIA') & (data.NACIONALIDAD!='VENEZUELA')].groupby('NACIONALIDAD').NACIONALIDAD.count().div(len(data[(data.NACIONALIDAD!='COLOMBIA') & (data.NACIONALIDAD!='VENEZUELA')]))
    plt.figure()
    nacionalidad.plot(kind='bar',xlabel='Nacionalidad',ylabel='Frecuencia (%)',title='Distribución nacionalidades')
    plt.show()

def generoestrato(data:pd.DataFrame,estrato:str)->None:#2
    """
    Crea un diagrama de torta de la distribución de género, esto según un estrato dado.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.
        estrato: Estrato.

    Retorno:
        Diagrama de torta apartir del Dataframe del icfes.


    """
    generoestrato=data[data.ESTRATO=='Estrato '+estrato].groupby('GENERO').GENERO.count() 
    generoestrato.plot(kind='pie',ylabel='Estudiantes',title='Diagrama de torta para el género de estrato '+estrato,autopct='%1.1f%%',shadow=True)#1autopct muestra el porcentaje
    plt.legend(loc='upper right')
    plt.show()
    
def desempenoalto(data:pd.DataFrame)->None:#3
    """
    Crea un diagrama de barras horizontal,de los 10 mejores promedios globales municipales,esto a partir del  DataFrame del icfes.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.

    Retorno:
        Diagrama de barras horizontal de los 10 mejores promedios globales por municipio.

    """
    desempeño=data.groupby('DEPARTAMENTO').PUNT_GLOBAL.mean().sort_values(ascending=False).head(10)
    desempeño=desempeño.sort_values()
    plt.figure()
    desempeño.plot(kind='barh',ylabel='Departamentos',xlabel='Promedio',title='Desempeño promedio Departamentos Colombianos')
    plt.show()

def desempenobajo(data:pd.DataFrame,Departamento:str)->None:#4
    """
    Crea un diagrama de barras horizontal,de los  5 peores promedios globales para un departamento dado.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.
        Departamento: Departamento a analizar.

    Retorno:
        Diagrama de barras horizontal de los 5 peores promedios globales por municipio(Se muestra para cada municipio el promedio por asignatura).

    """
    
    departamento = data[data.DEPARTAMENTO == Departamento]
    PUNT = departamento.groupby('MUNICIPIO').mean().sort_values(by = 'PUNT_GLOBAL').head()
    ordenado = PUNT.sort_values(by = 'PUNT_GLOBAL', ascending = False)
    reordenado = ordenado.iloc[:,:-1]    
    plt.figure()
    reordenado.plot(kind = 'barh', figsize = (10,5))
    plt.legend(loc= (1,0.4))
    plt.xlabel('Puntaje')
    plt.ylabel('Municipio')
    plt.show()
    return 'Gracias por utilizar la aplicación,ingrese una opción:'

def top(data:pd.DataFrame,categoria:str)->str:#5
    """
    Crea un diagrama de barras horizontal,de los 10 mejores promedios globales municipales por categoría(LECTURA,MATEMATICAS,NATURALES,SOCIALES,INGLES),esto a partir del  DataFrame del icfes.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.
        categoria: asignatura deseado a analizar.

    Retorno:
        Diagrama de barras horizontal de los 10 mejores promedios globales para la categoría dada.

    """
    x='Ingrese una opción validad (LECTURA,MATEMATICAS,NATURALES,SOCIALES,INGLES)'
    if categoria=='LECTURA':
        desempeño=data.groupby('MUNICIPIO').PUNT_LECTURA_CRITICA.mean().sort_values(ascending=False).head(10)
        x=1
        
    elif categoria=='MATEMATICAS':
        desempeño=data.groupby('MUNICIPIO').PUNT_MATEMATICAS.mean().sort_values(ascending=False).head(10)
        x=1

    elif categoria=='NATURALES':
        desempeño=data.groupby('MUNICIPIO').PUNT_NATURALES.mean().sort_values(ascending=False).head(10)
        x=1

    elif categoria=='SOCIALES':
        desempeño=data.groupby('MUNICIPIO').PUNT_SOCIALES.mean().sort_values(ascending=False).head(10)
        x=1

    elif categoria=='INGLES':
        desempeño=data.groupby('MUNICIPIO').PUNT_INGLES.mean().sort_values(ascending=False).head(10)
        x=1

    else:
        print(x)
        x=0
    if x==1:
        plt.figure()
        desempeño.plot(kind='barh',xlabel='Puntaje',ylabel='Municipio',title='DESEMPEÑO MUNICIPAL EN '+categoria)
        plt.show()
    return 'Gracias por utilizar la aplicación,ingrese una opción:'

        
def estratos(data:pd.DataFrame)->str:#6
    """
    Crea un diagrama de cajas y bigotes del promedio según estrato.


    Parámetros: 
        data: DataFrame que contiene la información del icfes.

    Retorno:
        Diagrama de cajas y bigotes del promedio según estrato.
    """

    plt.figure()
    data.boxplot(column = 'PUNT_GLOBAL', by = 'ESTRATO')
    plt.ylabel('Puntaje Global')
    plt.xlabel('Estrato')
    plt.title('')
    plt.show()
    return 'Gracias por utilizar la aplicación,ingrese una opción:'

def nutricion(data:pd.DataFrame,alimento:str,categoria=str)->None:#7
    """
    Crea un diagrama de cajas y bigotes del promedio de una asignatura(LECTURA,MATEMATICAS,NATURALES,SOCIALES,INGLES)
    según el consumo de un alimento dado(Proteínas, Lácteos y Frutos):

    Parámetros: 
        data: DataFrame que contiene la información del icfes.
        alimento:alimento deseado a analizar.
        categoria: asignatura deseado a analizar.

    Retorno:
        Diagrama de cajas y bigotes del promedio según estrato.
    """


    plt.figure() 
    data.boxplot(column = categoria, by = alimento, rot = '90', figsize = (10,5))
    plt.ylabel(categoria)
    plt.xlabel('Alimentacion')
    plt.xlabel('Alimentación')
    plt.ylabel('PUNT_'+categoria)
    plt.title('Diagrama de caja por '+alimento)
    plt.show()

def crear_matriz(data:pd.DataFrame)->tuple:#8
    '''
    Retorna una tupla que contiene la matriz, el diccionario de filas(estrato) y el diccionario de columnas(lectura)
    la matriz contiene información de estrato vs lectura.
    Parámetros: 
        data: DataFrame que contiene la información del icfes.
        

    Retorno:
        tupla que contiene la matriz, el diccionario de filas y el diccionario de columnas.
        Es decir: (matriz,dicestrato,diclectura).
    '''
    estratos = data["ESTRATO"].unique()
    estratos.sort()
    estratos_dict = dict(list(enumerate(estratos)))
    lectura = data["LECTURA_DIARIA"].unique()
    lectura.sort()
    aux = lectura[2]
    lectura[2] = lectura[1]
    lectura[1] = aux
    lectura_dict = dict(list(enumerate(lectura)))
    matriz=[]
    inf=data[["ESTRATO","LECTURA_DIARIA"]]
    for i in range(0,len(estratos_dict)):
        fila=[0]*len(lectura_dict)
        matriz.append(fila)
    for estrato in range(0,len(matriz)):
        for lectura in range(0,len(matriz[0])):
            repeticiones=len(inf[(inf['ESTRATO']==estratos_dict[estrato]) & (inf['LECTURA_DIARIA']==lectura_dict[lectura])])
            matriz[estrato][lectura]=repeticiones
            
    return (matriz,estratos_dict,lectura_dict)
  
def pruebaestrato(matriz:list,estrato:str)->int:#9
    '''Retorna el número de estudiantes que tomaron la prueba para un estrato dado del 1 al 6.
    Parámetros: 
        matriz: Matriz con la información de estrato vs lectura.
        estrato: estrato deseado a analizar.

    Retorno:
        Número de estudiantes del estrato dado que presentarón la prueba.'''
    estrato=int(estrato)
    filaestrato=matriz[estrato-1]
    total=0
    for cantidad in filaestrato:
        total+=cantidad
    return total

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
    return str(respuesta)

def mayorestrato(matriz:list)->str:#11
    '''Retorna el estrato que más presentó la prueba.
    Parámetros:
        matriz: Matriz con la información de estrato vs lectura.
    Retorno:
        Estrato que presentó el mayor número de estudiantes.'''
    dic={}
    for estrato in range(0,len(matriz)):
        dic[str(estrato+1)]=pruebaestrato(matriz,str(estrato+1))
    maximo=max(dic.values())
    estmax=0
    c=0
    while c==0:
        for estrato in dic:
            if dic[estrato]==maximo:
                estmax=estrato
                c=1
    return estmax

def mayorestratotiempolec(inf:tuple)->tuple:#12
    '''Retorna el estrato y el hábito de lectura más común en la prueba.
    Parámetros:
        tuple: tuple de la siguiente forma (matriz,dicestrato,diclectura).
    Retorno:
        Estrato y hábito de lectura más común en las pruebas icfes.'''

    matriz=inf[0]
    dic_estrato=inf[1]
    dic_lectura=inf[2]
    mayor=0
    estrato=None
    lectura=None
    for fila in range(0,len(matriz)):
        for columna in range(0,len(matriz[0])):
            valor=matriz[fila][columna]
            if valor>mayor:
                mayor=valor
                estrato=fila
                lectura=columna
    estrato=dic_estrato[estrato]
    lectura=dic_lectura[lectura]
    return estrato,lectura


         
    
        
    


        
    
    
    
    

    
    
    
    
    
        

        
        

    

        
        
  
    
    
   
    
  
    

       

    


    
    

    
    




 



    

    
        

   
        
        
        
        
    
        

