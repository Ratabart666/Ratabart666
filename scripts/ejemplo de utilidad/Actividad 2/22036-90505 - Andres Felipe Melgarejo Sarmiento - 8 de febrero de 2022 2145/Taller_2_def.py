# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:13:56 2022

@author: FELIP
"""

class complejos: 
    #Creamos la clase que contenga los atributos de los números complejos, es decir, una parte real y otra imaginaria 
    def __init__(self,real,imag):
        self.real= real
        self.imag=imag
        
    #Empezamos a definir las operaciones que vamos a aplicar sobre los números complejos
    def suma(self,other):
        a=self.real+other.real
        b=self.imag+other.imag
        return a,b
        
    def resta(self,other):
        c=self.real-other.real
        
        d=self.imag-other.imag
        
        return c,d
    
    def producto(self,other):
        d=((self.real*other.real)-(self.imag*other.imag))
        e=((self.imag*other.real)+(self.real*other.imag))
        return d,e
    
    def cociente(self,other):
        re=self.real
        re_=other.real
        im=self.imag
        im_=other.imag
        
        f= ((re*re_)+(im*im_))/(re_**2 + im_**2)
        g= ((im*re_)-(re*im_))/(re_**2 + im_**2)
        
        return f,g
    
    def norma(self):
        re=self.real
        im=self.imag
        
        
        h=(((re**2)+(im**2))**(1/2))
        return h
 
print("Pruebas suma: ")
n1= complejos(3,2)
n2 = complejos(1,1)
print(n1.suma(n2))

n3 = complejos(6,4)
n4 = complejos(9,1)
print(n3.suma(n4))

print("Pruebas resta: ")
numero = complejos(3,7)
n2 = complejos(1,4)
print(numero.resta(n2))

numero = complejos(4,6)
n2 = complejos(2,6)
print(numero.cociente(n2))

print("Pruebas producto: ")
numero = complejos(5,6)
n2 = complejos(9,4)
print(numero.producto(n2))

numero = complejos(5,1)
n2 = complejos(3,7)
print(numero.producto(n2))

print("Pruebas cociente: ")
numero = complejos(7,6)
n2 = complejos(1,4)
print((numero.cociente(n2)))

numero = complejos(9,4)
n2 = complejos(4,8)
print(numero.cociente(n2))

print("Pruebas norma: ")
numero = complejos(4,6)
print(round(numero.norma(),2))

numero = complejos(1,9)
print(round(numero.norma(),2))

"Algunas propiedades de las operaciones entre complejos fueron sacadas de: https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/operations-with-complex-numbers"