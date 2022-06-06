#!/usr/bin/env python
# coding: utf-8

# In[89]:


#primero creamos la clase en la cual vamos a trabajar todas las operaciones de numeros complejos
class compleja:
    def __init__(self,Re,Im): #definimos el numero complejo con su parte real y parte imaginaria
        self.Re=Re
        self.Im=Im
    def suma(self,other): #definimos la función que nos va a hacer la suma de dos complejos self + other
        c=self.Re+other.Re #colocamos en una variable c la suma de la parte real de mis dos numeros complejos
        d=self.Im+other.Im #colocamos en una variable d la suma de la parte imaginaria de mis dos numeros complejos
        return compleja(c,d) 
    def imprimir_suma(self):#imprimos en un formato legible nuestro complejo
        print (f"{self.Re}+{self.Im}i")
    def resta(self,other): #definimos la funcion que nos va a hacer la resta de dos complejos
        c=self.Re-other.Re #colocamos en una variable c la resta de la parte real de mis dos numeros complejos
        d=self.Im-other.Im #colocamos en una variable d la resta de la parte imaginaria de mis dos numeros complejos
        return compleja(c,d)
    def imprimir_resta(self):#imprimos en un formato legible nuestro complejo
        print (f"{self.Re}-{self.Im}i")
    def producto(self,other): #definimos la funcion que nos va a hacer el producto de dos complejos
        c=(self.Re*other.Re) - (self.Im*other.Im) #colocamos en una variable c el proceso a (ac-bd)
        d=(self.Re*other.Im) + (self.Im*other.Re)#colocamos en una variable d el proceso (ad+bc)
        return compleja(c,d)
    def imprimir_producto(self):#imprimos en un formato legible nuestro complejo
        print (f"{self.Re}+{self.Im}i")
    def cociente(self,other):#definimos la funcion que nos va a hacer el cociente entre dos complejos
        c=(((self.Re*other.Re)+(self.Im*other.Im)) / ((other.Re**2)+(other.Im**2)))
        d=(((self.Im*other.Re)-(self.Re*other.Im)) / ((other.Re**2)+(other.Im**2)))
        
        return compleja(c,d)
    def imprimir_cociente(self):#imprimos en un formato legible nuestro complejo
        print (f"{self.Re}+{self.Im}i")
    def norma(self): #definimos la funcion que nos permite calcular la norma de un numero complejo (pitagoras)
        n= ((((self.Re)**2)+((self.Im)**2))**0.5)
        
        return n #no hay necesidad de una funcion de formato porque esta funcion me da un numero real
                


# In[8]:


z1=compleja(1,2)#1+2i
z2=compleja(2,3)#2+3i
(z1.suma(z2)).imprimir_suma()


# In[9]:


z1=compleja(3,4)
z2=compleja(4,5)
(z1.suma(z2)).imprimir_suma()


# In[12]:


z1=compleja(5,7)
z2=compleja(4,5)
(z1.resta(z2)).imprimir_resta()


# In[13]:


z1=compleja(2,3)
z2=compleja(4,1)
(z1.resta(z2)).imprimir_resta()


# In[19]:


z1=compleja(1,2)
z2=compleja(2,3)
(z1.producto(z2)).imprimir_producto()


# In[20]:


z1=compleja(5,7)
z2=compleja(4,5)
(z1.producto(z2)).imprimir_producto()


# In[27]:


z1=compleja(5,7)
z2=compleja(4,5)
(z1.cociente(z2)).imprimir_cociente()


# In[28]:


z1=compleja(6,2)
z2=compleja(2,1)
(z1.cociente(z2)).imprimir_cociente()


# In[90]:


z1=compleja(5,5)
z1.norma()


# In[91]:


z1=compleja(3,4)
z1.norma()


# In[ ]:





# In[ ]:




