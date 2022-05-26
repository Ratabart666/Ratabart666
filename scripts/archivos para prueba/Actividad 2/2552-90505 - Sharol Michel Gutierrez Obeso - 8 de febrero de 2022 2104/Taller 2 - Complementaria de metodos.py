#!/usr/bin/env python
# coding: utf-8

# In[150]:


#TAREA 2 - COMPLEMENTARIA DE METODOS COMPUTACIONALES - SHAROL GUTIERREZ - 201819940
import numpy #Fue necesario importar esta biblioteca para definir las funciones de producto y cociente entre numeros complejos, ademas de la norma de un numero complejo. 
class complejos: #Esta clase contiene a los numeros complejos, es decir, numeros con una parte real y una parte imaginaria
    def __init__ (self,re,im): #Este metodo define la clase y sus componentes. Los numeros complejos tienen parte real (re) y parte imaginaria(im).
        self.re = re #con esto definimos a la parte real del numero complejo
        self.im = im #Con esto definimos la parte imaginaria del numero complejo
    def suma (self,otro): #Este metodo define la suma entre numeros complejos, sabiendo que en estos numeros la parte real se suma con la parte real y la parte imaginaria se sume con la imaginaria.
        realsum = self.re+otro.re #Se plantea la parte real de la suma entre complejos. 
        imaginariasum = self.im+otro.im #Se plantea la parte imaginaria de la suma entre complejos. 
        return realsum, imaginariasum #Se retornan los resultados. 
    def resta (self,otro): #Metodo que define la resta entre numeros complejos.
        realres = self.re-otro.re #Parte real de la resta 
        imaginariares = self.im-otro.im #Parte imaginaria de la resta 
        return realres, imaginariares #Se retornan los resultados previamente programados 
    def producto (self,otro): #Se define el producto punto entre numeros complejos
        realpro = numpy.dot(self.re,otro.re)-numpy.dot(self.im,otro.im) #Parte real del producto punto. 
        imaginariapro = numpy.dot(self.re,otro.im)+numpy.dot(self.im,otro.re) #Parte imaginaria del producto punto. 
        return realpro, imaginariapro #Se retorna lo planteado
    def cociente (self,otro): #Se define la operacion cociente entre numeros complejos
        realco = (numpy.dot(self.re,otro.re)+numpy.dot(self.im,otro.im))/(otro.re**2+otro.im**2) #Se define la parte real del cociente entre complejos.
        imaginarioco = (numpy.dot(self.im,otro.re)-numpy.dot(self.re,otro.im))/(otro.re**2+otro.im**2) #Se define la parte imaginaria del cociente entre complejos. 
        return realco, imaginarioco #se retorna lo obtenido
    def norma (self): #Metodo que define la norma de un numero complejo
        renorma = numpy.sqrt(self.re**2+self.im**2) #Se plantea la norma
        return renorma #Se retorna lo obtenido 


# In[151]:


#EJEMPLOS DE SUMA
z1 = complejos(1,2) #Ejemplo 1 de suma entre complejos. Se definen los dos numeros y se aplica la operacion.  
z2 = complejos(2,3)
z1.suma(z2)


# In[152]:


z3 = complejos(2,4) #Ejemplo 2 de suma entre complejos. Se definen los dos numeros y se aplica la operacion.
z4 = complejos(5,7)
z3.suma(z4)


# In[153]:


z5 = complejos(5,2) #Ejemplo 1 de resta entre complejos. Se definen los dos numeros y se aplica la operacion.
z6 = complejos(2,5)
z5.resta(z6)


# In[154]:


z7 = complejos(6,2) #Ejemplo 2 de resta entre complejos. Se definen los dos numeros y se aplica la operacion.
z8 = complejos(2,9)
z7.resta(z8)


# In[155]:


z9 = complejos(3,2) #Ejemplo 1 de producto entre complejos. Se definen los dos numeros y se aplica la operacion.
z10 = complejos(2,3)
z9.producto(z10)


# In[156]:


z11 = complejos(5,2) #Ejemplo 2 de producto entre complejos. Se definen los dos numeros y se aplica la operacion.
z12 = complejos(0,3)
z11.producto(z12)


# In[157]:


z13 = complejos(2,2) #Ejemplo 1 de cociente entre complejos. Se definen los dos numeros y se aplica la operacion.
z14 = complejos(2,-4)
z13.cociente(z14)


# In[158]:


z15 = complejos(-1,2) #Ejemplo 2 de cociente entre complejos. Se definen los dos numeros y se aplica la operacion.
z16 = complejos(2,4)
z15.cociente(z16)


# In[159]:


z9 = complejos(2,2) #Ejemplo 1 del calculo de la norma de un complejo. Se define el numero y se aplica la operacion.
z9.norma()


# In[160]:


z9 = complejos(1,2) #Ejemplo 1 del calculo de la norma de un complejo. Se define el numero y se aplica la operacion.
z9.norma()


# In[ ]:



   
   
   

