#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:13:57 2022

@author: julianklinger
"""

class complejos: #Se define la clase
    def __init__(self, real, imaginario): #Se definen los atributos de la clase
        self.real = real                  #como es la parte real e imaginaria
        self.imaginario = imaginario      #del numero complejo
        
        # Se definen los metodos, que son las operaciones
    def suma(self,other):
        a = self.real + other.real
        b = self.imaginario + other.imaginario
        return a,b
    
    def resta(self,other):
        a = self.real - other.real
        b = self.imaginario - other.real
        return a,b
    
    def multiplicacion(self,other):
        a =(self.real * other.real) - (self.imaginario * other.imaginario)
        b = (self.real * other.imaginario) + (self.imaginario * other.real)
        return a,b
    
    def division(self,other):
        sr = self.real
        si = self.imaginario
        ore = other.real
        oi = other.imaginario
        a = ((sr*ore) + (sr*oi))/((ore*ore)+(oi*oi))
        b = ((si*ore)+(sr*oi))/((ore*ore)+(oi*oi))
        a_r = round(a,2)
        b_r = round(b,2)
        return a_r,b_r
    
    def norma(self):
        a = ((self.real*self.real) + (self.imaginario * self.imaginario))**(1/2)
        return a
    
    #EJEMPLOS/PRUEBAS

n1 = complejos(5,2) #Se crean los objetos sobre los cuales se van a aplicar
n2 = complejos(1,1) #los metodos
n3 = complejos(5,6)
n4 = complejos(9,2)
print("EJEMPLOS")
print("Todos los numeros estan en formato (parte_real , parte_imaginaria)")
print("(5,2) + (1,1) = ", n1.suma(n2)) #Se llama a los metodos a actuar sobre
print("(5,2) - (1,1) = ",n1.resta(n2)) #los objetos, con sus respectivos parametros
print("(5,2) x (1,1) = ",n1.multiplicacion(n2))
print("(5,2) / (1,1) = ",n1.division(n2))
print("norma (5,2) = ", round(n1.norma(),2))

print("(5,6) + (9,2) = ", n3.suma(n4))
print("(5,6) - (9,2) = ",n3.resta(n4))
print("(5,6) x (9,2) = ",n3.multiplicacion(n4))
print("(5,6) / (9,2) = ",n3.division(n4))
print("norma (9,2) = ", round(n4.norma(),2))








