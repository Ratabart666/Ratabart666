#!/usr/bin/env python
# coding: utf-8

# In[212]:


#Datos y programas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
plt.style.use('dark_background')


datos=pd.read_csv('datos_termodinamicos.txt')
pd.set_option('display.max_columns', 999)


def productoria(list):
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues*list[i]
    return despues
def sumatoria(list):
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues+list[i]
    return despues
        

def interpolacionlagrange(x,X,Y):#Por favor que x tenga igual numeros de puntos que y
    coeficientes=Y
    polinomios_x=[]
    auxiliar=[]
    for i in np.arange(0,len(X)):
        for j in np.arange(0,len(X)): 
            if i!=j:
                auxiliar.append((x-X[j])/(X[i]-X[j]))
        polinomios_x.append(productoria(auxiliar)*coeficientes[i])
        auxiliar=[]
    return sumatoria(polinomios_x)


# In[223]:

print('------------------------------------------------')
print('Datos')
print(datos)
print('------------------------------------------------')

T=datos['T(C)'].tolist()
P=datos['Pvap(kPa)'].tolist()
Vg=datos['satliq(m**3/kg)'].tolist()
vf=datos['satvapor(m**3/kg)'].tolist()
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,P)
ax.set_title('Gráfica:T(°C) vs Pvap(Kpa)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('Pvap(Kpa)')
plt.show()


# In[220]:

fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,Vg)
ax.set_title('Gráfica: T(°C) vs satliq(m**3/kg)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('satliq(m**3/kg)')
plt.show()


# In[221]:


fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,vf)
ax.set_title('Gráfica: T(°C) vs satvapor(m**3/kg)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('satvapor(m**3/kg)')
plt.show()




# In[213]:


#A manera de ejemplo, tomaremos 3 puntos y hallaremos el polinomio de Lagrange asociado a dichos puntos (P vs T). 
#Así mismo hallaremos el polinomio asociado por sympy. +10 puntos.
T=datos['T(C)'].tolist()[0:3]
P=datos['Pvap(kPa)'].tolist()[0:3]
print('El polinomio interpolador de lagrange para los 3 primeros puntos de T vs Pvap es:')
print(lagrange(T,P))
print('------------------------------------------------')



# In[214]:


#Tabla Interpolación de P vs T, utilizando valores intermedios de temperatura.
#Para esto generalice el programa del punto 1. +15

T=np.arange(10,202.5,2.5)
P=interpolacionlagrange(T,datos['T(C)'].tolist(),datos['Pvap(kPa)'].tolist())
datosinterpolados=pd.DataFrame()
datosinterpolados['T(C)']=T
datosinterpolados['Pvap(Kpa)']=P
datosinterpolados['Pvap(Kpa)']=datosinterpolados['Pvap(Kpa)'].round(4)
print('Estos son los datos interpolados P vs T')
print(datosinterpolados)



# In[215]:


#Tabla Interpolación de Vg vs T.+5
Vf=interpolacionlagrange(T,datos['T(C)'].tolist(),datos['satliq(m**3/kg)'].tolist())
datosinterpolados['satliq(m**3/kg)']=Vf
datosinterpolados['satliq(m**3/kg)']=datosinterpolados['satliq(m**3/kg)'].round(6)
print('------------------------------------------------')
print('Estos son los datos interpolados vg vs T')
print(print(datosinterpolados[['T(C)','satliq(m**3/kg)']].head(60)))
print(print(datosinterpolados[['T(C)','satliq(m**3/kg)']].tail(17)))


# In[216]:


#Tabla Interpolación de Vf vs T.+5
Vg=interpolacionlagrange(T,datos['T(C)'].tolist(),datos['satvapor(m**3/kg)'].tolist())
datosinterpolados['satvapor(m**3/kg)']=Vg
datosinterpolados['satvapor(m**3/kg)']=datosinterpolados['satvapor(m**3/kg)'].round(5)
print('------------------------------------------------')
print('Estos son los datos interpolados vf vs T')
print(print(datosinterpolados[['T(C)','satvapor(m**3/kg)']].head(60)))
print(print(datosinterpolados[['T(C)','satvapor(m**3/kg)']].tail(17)))


# In[217]:

print('------------------------------------------------')
print('Estos son los datos interpolados(todo)')
print(datosinterpolados.head(60))
print(datosinterpolados.tail(17))


# In[218]:


T=datosinterpolados['T(C)'].tolist()
P=datosinterpolados['Pvap(Kpa)'].tolist()
Vg=datosinterpolados['satliq(m**3/kg)'].tolist()
vf=datosinterpolados['satvapor(m**3/kg)'].tolist()


# In[219]:


#Gráficas en formato png.  Los ejes deben aparecer debidamente identificados
#y el tamaño de las etiquetas debe ser visible. +10
fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,P)
ax.set_title('Gráfica interpolada:T(°C) vs Pvap(Kpa)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('Pvap(Kpa)')
plt.show()


# In[220]:


fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,Vg)
ax.set_title('Gráfica interpolada: T(°C) vs satliq(m**3/kg)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('satliq(m**3/kg)')
plt.show()


# In[221]:


fig, ax = plt.subplots(figsize=(20,10))
ax.plot(T,vf)
ax.set_title('Gráfica interpolada: T(°C) vs satvapor(m**3/kg)')
ax.set_xlabel('T(°C)')
ax.set_ylabel('satvapor(m**3/kg)')
plt.show()


# In[222]:

print('------------------------------------------------')
print('Análisis de resultados y conclusiones. +5')
print('Analizando,es evidente que existen resultados incoherentes(Vf,Vg,Pvap negativos),esto nos indica que')
print('la interpolación de lagrange sobre-justa, por ende tenemos como conclusión que este metódo no es muy útil para')
print('una gran cantidad de datos,por ende para finalizar, se infiere que es mejor utilizar regresión por minimos cuadrados.')



