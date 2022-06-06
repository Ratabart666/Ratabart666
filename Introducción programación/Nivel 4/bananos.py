import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(nombrearchivo:str)->pd.DataFrame:
    archivo=pd.read_csv(nombrearchivo)
    return archivo
archivo=cargar_datos('exportaciones.csv')

def graficar_datos(archivo)->None:#1
    x=archivo.groupby('Producto').ValorMilesDolar.sum()
    x=archivo.groupby('Producto').ValorMilesDolar.sum()
    plt.figure()
    x.plot(kind='pie',figsize=(10,5))
    plt.show()
    
    
    return x

def graficar_datos_Cavendish_Valery(archivo)->None:
    x=archivo.groupby('Producto').ValorMilesDolar.sum()
    x=archivo[archivo.Producto!='Cavendish Valery'].groupby('Producto').ValorMilesDolar.sum()
    plt.figure()
    x.plot(kind='bar',figsize=(10,5))
    plt.show()
    
def anios_y_kilos_reportados(archivo)->str:
    anio=archivo['Anio'].unique()
    anio=sorted(list(anio))
    x=None
    print('Reporte de exportaciones por año y departamento')
    print('-----------------------------')
    for fecha in anio:
        print('-----------------------------')
        print(fecha)
        print('-----------------------------')
        x=archivo[archivo.Anio==fecha].groupby('DepartamentoOrigen').Cantidad.sum()
        print(x)
        
    return 'Gracias por utilizar la aplicación' 

def evolucion_mercado_bananos(archivo,moneda:str)->None:
    if moneda=='Dolar':
            x=archivo.groupby('Anio').ValorMilesDolar.sum()
            plt.figure()
            x.plot(kind='bar',figsize=(10,5))
            plt.xlabel('Año')
            plt.ylabel('Valor Miles de dolares')
            plt.show()
    elif moneda=='Peso':
            x=archivo.groupby('Anio').ValorMilesPesos.sum()
            plt.figure()
            x.plot(kind='bar',figsize=(10,5))
            plt.xlabel('Año')
            plt.ylabel('Valor Miles de pesos')
            plt.show()
    else:
        print('Ingrese la moneda que desea(Dolar o Peso)')

def top_paises(archivo)->str:
    x=archivo.groupby('PaisDestino').Cantidad.sum()
    y=x.sort_values()
    x=x.sort_values(ascending=False)
    x=x[0:5]
    y=y[0:5]
    print(x)
    print('-----')
    print(y)
    x.plot(kind='barh',figsize=(10,5),color='orange')
    plt.xlabel('Cantidad (kg*10**9)')
    plt.ylabel('Países')
    plt.title('Los 5 países que mas importan bananos Colombianos')
    plt.show()
    return 'Gracias por utilizar la aplicación' 

    
    


            
            
        
        

        

   
    

    


