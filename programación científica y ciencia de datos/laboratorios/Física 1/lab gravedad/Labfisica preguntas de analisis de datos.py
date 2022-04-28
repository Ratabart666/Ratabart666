# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:26:59 2021

@author: Asus
"""

import numpy as np
import pandas as pd
listamasaprueba=[0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2]#[Kilogramos]
listatension1=[1.503,1.57,1.591,1.601,1.622,1.635,1.61,1.645,1.669,1.683,1.723]#[Newtons]
listatethagrados=[70,67,66,65,64,62,61,59,57,55,54,]#grados
listaphigrados=[18,21,24,26,29,30,31,32,33,35,36]#grados


def fuerzatotal(listamasaprueba,listatension1,listatethagrados,listaphigrados)->pd.DataFrame:#Punto 1,2
    numerodedatos=len(listamasaprueba)
    listaSumFx=[]
    listaSumFy=[]
    for indice in range(numerodedatos):
        T1=listatension1[indice]
        m=listamasaprueba[indice]
        tetharadianes=np.radians(listatethagrados[indice])
        phiradianes=np.radians(listaphigrados[indice])
        M=0.150#kg,VALOR TEÓRICO MASA M
        g=9.80#m/s**2 VALOR TEÓRICO GRAVEDAD TERRESTRE
        T2=M*g#N
        SumFx=T2*np.cos(phiradianes)-T1*np.sin(tetharadianes)#N
        SumFy=T2*np.sin(phiradianes)+T1*np.cos(tetharadianes)-m*g#N
        listaSumFx.append(SumFx)
        listaSumFy.append(SumFy)
        Fuerzatotalx=pd.Series(listaSumFx)
        Fuerztotaly=pd.Series(listaSumFy)
        Datos=pd.DataFrame({'Sumatoria fuerzas eje x(N)':Fuerzatotalx,'Sumatoria fuerzas eje y(N)':Fuerztotaly})
    return Datos.describe()
print(fuerzatotal(listamasaprueba, listatension1, listatethagrados, listaphigrados))
                #Punto 3
# En media la ''Fuerza total en el eje x'' es del orden de una décima de newton y en media la ''Fuerza total en el eje y''
# es del orden de una mílesma de Newton, adicionalmente podemos observar por std(desviación estandar) que los datos son precisos
#,es decir estan ''muy cercanos''.
                #Punto 4
# Queda entonces verificada experimentalmente la primera ley de Newton, ya que como podemos ver la sumatoria de todas las fuerzas es
# aproximadamente 0. En el caso del analisis del error sistemático y aleatorío, el primero hace referencia a aquellas fallas en la medición ocasionadas
# por la técnica experimental o calibración del instrumento; el error aleatorio se debe debido a fluctuaciones estadísticas en el muestreo de los Datos.
# Queda como conclusión que para mejorar nuestro experimento debemos proponer técnicas experimentales mas sensibles

                #Punto 5 (El despeje de las formúlas está adjunto)
# Despejando queda que g=(T1/m)*(sen(tetha)*tan(phi)+cos(tetha)) y M=m(sen(tetha)/(sen(tetha)*tan(phi)+cos(tetha)))
# angúlos se pasan a radianes ya que la implementación en pyhton tiene como entrada radianes
def calcular_M_y_g_experimentalmente(listamasaprueba,listatension1,listatethagrados,listaphigrados)->pd.DataFrame:
    numerodedatos=len(listamasaprueba)
    listag=[]
    listaM=[]
    for indice in range(numerodedatos):
        T1=listatension1[indice]#N
        m=listamasaprueba[indice]#kg
        tetharadianes=np.radians(listatethagrados[indice])
        phiradianes=np.radians(listaphigrados[indice])
        g=(T1/m)*((np.sin(tetharadianes)*np.tan(phiradianes))+np.cos(tetharadianes))#m/s**2
        M=m*((np.sin(tetharadianes))/(np.sin(tetharadianes)*np.tan(phiradianes)+np.cos(tetharadianes)))#kg
        listag.append(g)
        listaM.append(M)
        gravedad=pd.Series(listag)
        MasaM=pd.Series(listaM)
        Datos=pd.DataFrame({'Gravedad terrestre(m/s**2)':gravedad,'Masa M(kg)':MasaM})
    return Datos.describe()
print('--')
print(calcular_M_y_g_experimentalmente(listamasaprueba, listatension1, listatethagrados, listaphigrados))

# Analizando el analisís estadistico y teniendo en cuenta que el número de cifras de las operaciones(2), tenemos, el siguiente resultado experimental:
    # g=10(m/s**2)+-0.4(m/s**2)
    # M=0.14kg+-(0.003)=> (aproximadamente igual a: 0.14kg). Vemos que el resultado teoríco y experimental son muy cercanos, esto lo podemos cuantificar con el error relativo:
    #error relativo(%) g= ((10m/s**2)-9.80(m/s**2))/9.8(m/s**2)*100%=2%
    #error relativo(%) m=((0.15kg)-(0.14kg))/(0.15kg)*100%=6.7%




