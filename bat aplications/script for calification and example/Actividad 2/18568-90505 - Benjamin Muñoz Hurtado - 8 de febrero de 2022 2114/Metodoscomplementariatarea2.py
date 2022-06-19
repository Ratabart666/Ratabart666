#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:13:15 2022

@author: Benjamin
"""

class compleja:
    def __init__ (self,real,imaginaria):
        self.real=real
        self.imaginaria=imaginaria
        
    def suma(self, other):
        
        real=self.real+other.real
        imaginaria=self.imaginaria+other.imaginaria
        suma=compleja(real, imaginaria)
       
        return suma

    def resta(self,other):

        real=self.real-other.real
        imaginaria=self.imaginaria-other.imaginaria
        resta=compleja(real,imaginaria)

        return resta
    
    def multiplicacion(self,other):
        
        real=(self.real*other.real)-(self.imaginaria*other.imaginaria)
        imaginaria=(self.real*other.imaginaria)+(self.imaginaria*other.imaginaria)
        
        multiplicacion=compleja(real,imaginaria)
        
        return multiplicacion
        
    def cociente (self, other):
        
        real=(self.real*other.real+self.imaginaria*other.imaginaria)/(((other.real)**2)+((other.imaginaria)**2))
        imaginaria=(self.imaginaria*other.real-self.real*other.imaginaria)/(((other.real)**2)+((other.imaginaria)**2))
        
        cociente=compleja(real, imaginaria)
        
        return cociente
    
    def norma (self):
        
        norma=(((self.real)**2)+((self.imaginaria**2)))**(1/2)
        
        return norma
    
    def imprimir(self):
        
        numero=str(self.real)+" + "+str(self.imaginaria)+"i"
        
        return numero
#ejemplo suma 1
numero_1=compleja(1,3) #Un numero complejo en formato (x,y) significa x+iy
numero_2=compleja(2,4) #Este por ejemplo es 2+4i
print((numero_1.suma(numero_2)).imprimir()) #Esto se usa para sumar numeros y mostrar resultado como un string

#ejemplo suma 2
numero_1=compleja(4,6) 
numero_2=compleja(1,2) 
print((numero_1.suma(numero_2)).imprimir())

#ejemplo resta 1
numero_1=compleja(8,9) 
numero_2=compleja(1,1) 
print((numero_1.resta(numero_2)).imprimir())

#ejemplo resta 2
numero_1=compleja(6,3) 
numero_2=compleja(5,5) 
print((numero_1.resta(numero_2)).imprimir())

#ejemplo multiplicación 1
numero_1=compleja(3,10) 
numero_2=compleja(4,1) 
print((numero_1.multiplicacion(numero_2)).imprimir())

#ejemplo multiplicación 2
numero_1=compleja(7,13) 
numero_2=compleja(12,6) 
print((numero_1.multiplicacion(numero_2)).imprimir())

#ejemplo cociente 1
numero_1=compleja(2,7) 
numero_2=compleja(3,2) 
print((numero_1.cociente(numero_2)).imprimir())

#ejemplo cociente 2
numero_1=compleja(3,2) 
numero_2=compleja(2,7) 
print((numero_1.cociente(numero_2)).imprimir())

#ejemplo norma 1
numero_1=compleja(3,4) 
print(numero_1.norma())#Este no necesita .imprimir ya que el resultado de la norma es un float

#ejemplo norma 2
numero_1=compleja(1,1) 
print(numero_1.norma())
