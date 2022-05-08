#!/usr/bin/env python
# coding: utf-8

# In[73]:


import math as m # Importamos la libreria math para usar la raiz cuadrada en la operacion de la norma del numero complejo

class complejos: # Definimos la clase del numero complejo
    def __init__(self,real,complejo): # Usando la funcion __init__ definimos 2 atributos de un numero complejo su parte real y compleja
        self.real = real
        self.complejo = complejo

    def suma(self,complejo): # Creamos la funcion suma de dos numeros complejos
        s1=self.real+complejo.real # Operamos la parte real
        s2=self.complejo+complejo.complejo # Operamos la parte complejos
        if s2>0:
            a="+"
        else:
            a=""
        if complejo.complejo > 0:
            b="+"
        else:
            b=""
        if self.complejo > 0:
            c="+"
        else:
            c="" # Establecemos los signos de los numeros para que la presentacion en al momento de imprimir sea adecuada
        print("siendo los numeros "+str(self.real)+c+str(self.complejo)+"i"+" y "+str(complejo.real)+b+str(complejo.complejo)+"i"+" El resultado de su suma es: "+str(s1)+a+str(s2)+"i\n") #Mostramos los numeros y el resultado de su operacion
        return(complejos(s1,s2))
    
    def resta(self,complejo):
        r1=self.real-complejo.real # Operamos la parte real
        r2=self.complejo-complejo.complejo # Operamos la parte compleja
        if r2>0:
            a="+"
        else:
            a=""
        if complejo.complejo > 0:
            b="+"
        else:
            b=""
        if self.complejo > 0:
            c="+"
        else:
            c="" # Establecemos los signos de los numeros para que la presentacion en al momento de imprimir sea adecuada
        print("Siendo los numeros "+str(self.real)+c+str(self.complejo)+"i"+" y "+str(complejo.real)+b+str(complejo.complejo)+"i"+" El resultado de su resta es: "+str(r1)+a+str(r2)+"i\n") # Mostramos los numeros y el resultado de su operacion
        return(complejos(r1,r2))
    
    def producto(self,complejo):
        m1=(self.real*complejo.real)-(self.complejo*complejo.complejo) # Operamos para obtener la parte real
        m2=(self.real*complejo.complejo)-(self.complejo*complejo.real)  # Operamos para obtener la parte compleja
        if m2>0:
            a="+"
        else:
            a=""
        if complejo.complejo > 0:
            b="+"
        else:
            b=""
        if self.complejo > 0:
            c="+"
        else:
            c="" # Establecemos los signos de los numeros para que la presentacion en al momento de imprimir sea adecuada
        print("Siendo los numeros "+str(self.real)+c+str(self.complejo)+"i"+" y "+str(complejo.real)+b+str(complejo.complejo)+"i"+" El resultado del producto es: "+str(m1)+a+str(m2)+"i\n") # Mostramos los numeros y el resultado de su operacion
        return(complejos(m1,m2))
    
    def cociente(self,complejo):
        c1=((self.real*complejo.real)+(self.complejo*complejo.complejo))/(((complejo.real)**2)+((complejo.complejo)**2))  # Operamos para obtener la parte real
        c2=((self.complejo*complejo.real)-(self.real*complejo.complejo))/((((complejo.real)**2)+(complejo.complejo)**2))  # Operamos para obtener la parte compleja
        if c2>0:
            a="+"
        else:
            a=""
        if complejo.complejo > 0:
            b="+"
        else:
            b=""
        if self.complejo > 0:
            c="+"
        else:
            c="" # Establecemos los signos de los numeros para que la presentacion en al momento de imprimir sea adecuada
        print("Siendo los numeros "+str(self.real)+c+str(self.complejo)+"i"+" y "+str(complejo.real)+b+str(complejo.complejo)+"i"+" El resultado de la division es: "+str(round(c1,2))+a+str(round(c2,2))+"i\n") # Mostramos los numeros y el resultado de su operacion
        return(complejos(c1,c2))
    
    def norma(self):
        n=m.sqrt((self.real)**2+(self.complejo)**2) # Aplicamos la formula de la norma de un vector ya que un numero complejo puede verse como vector
        if self.complejo > 0:
            a="+"
        else:
            a="" # Establecemos el signo del numero para que la presentacion en al momento de imprimir sea adecuada
        print("siendo el numero "+str(self.real)+a+str(self.complejo)+"i"+" El resultado de la norma es: "+str(round(n,2))+"\n") # Mostramos los numeros y el resultado de su operacion
        return(n)

# En todas las funciones recurrimos a la clase del numero complejo para poder asiganar a cada uno su parte real y compleja de forma que se desarrollen las operaciones de manera adecuada

# Posteriormente emplearemos 4 numeros complejos para los ejemplos de las distintas funciones

a=complejos(2,2)
b=complejos(1,-1)
c=complejos(-4,7)
d=complejos(1,-8)
print("Pruebas de las operaciones \n ")
print("Prueba de la Suma: \n ")
print(a.suma(b))
print(c.suma(d)) 
print("Prueba de la Resta: \n ")
print(a.resta(b))
print(c.resta(d))
print("Prueba del Producto: \n ")
print(a.producto(b))
print(c.producto(d))
print("Prueba del Cociente: \n ")
print(a.cociente(b))
print(c.cociente(d))
print("Prueba de la Norma: \n ")
print(a.norma())
print(b.norma())


# In[ ]:





# In[ ]:




