# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:09:04 2022

@author: ASUS
"""

class numero_complejo:
    """Es la clase para los numero complejos, tnedrá atributos los cuales son
    sus operaciones, cada numero tienen una parte real y una imaginaria"""
    def __init__(self, real, imaginario): #Constructor de la clase
        self.real = real
        self.imaginario = imaginario
        
    def sumar(self, numero_complejo2): #Atributo de suma para sumar 2 numero complejos
        real1 = self.real
        real2 = numero_complejo2.real
        imag1 = self.imaginario
        imag2 = numero_complejo2.imaginario
        real = real1 + real2
        imag = imag1 + imag2
        print(f"el numero resultante es {real} + {imag}i")
        return(numero_complejo(real,imag))
        
    def restar(self, numero_complejo2): #Atributo de resta para la diferencia de 2 numeros complejos
        real1 = self.real
        real2 = numero_complejo2.real
        imag1 = self.imaginario
        imag2 = numero_complejo2.imaginario
        real = real1 - real2
        imag = imag1 - imag2
        print(f"el numero resultante es {real} + {imag}i")
        return(numero_complejo(real,imag))
    
    def norma(self): #Atributo de norma para calcular la norma de un numero complejo
        real1 = self.real
        imag1 = self.imaginario
        real = real1**2
        imag = imag1**2
        norma = (real+imag)**(1/2)
        print(f"la norma del numero complejo ingresado es {norma}")
        return(norma)
    
    def producto(self, numero_complejo2): 
        #Atributo de producto para calcular el producto de 2 numeros complejos
        real1 = self.real
        real2 = numero_complejo2.real
        imag1 = self.imaginario
        imag2 = numero_complejo2.imaginario
        real = (real1 * real2)- (imag2*imag1)
        imag = (real1*imag2) + (imag2*real1)
        if imag > 0:
            print(f"el numero resultante del producto es {real} + {imag}i")
        else:
            print(f"el numero resultante del producto es {real} {imag}i")
        
        return(numero_complejo(real,imag))
    
    def division(self, numero_complejo2):
        #Atributo de division para calcular el cociente de 2 numeros complejos
        numero_complejo2 = numero_complejo(numero_complejo2.real,((numero_complejo2.imaginario)*(-1)) )
        arriba= self.producto(numero_complejo2)
        real = arriba.real
        imag = arriba.imaginario
        abajo = ((numero_complejo2.real)**2)+((numero_complejo2.imaginario)**2)
        print(f"el numero resultante es ({real} + {imag}i)/{abajo}")
        
print("Bienvenido al programa de los numero complejos, acontinuación daremos ejemplos de sus operaciones: ")
print("Primero definiremos 4 numeros complejos distintos y los llamaremos con z y el subindice correspondiente del 1 al 4")
z1 = numero_complejo(3, 4)
z2 = numero_complejo(5, 3)
z3 = numero_complejo(8, 1)
z4 = numero_complejo(9, 5)
print("Estos numeros son:")
print("z1 = 3 + 4i")
print("z2 = 5 + 3i")
print("z3 = 8 + 1i")
print("z4 = 9 + 5i")

print("ahora trabajaremos sobre la suma con dos ejemplos")
print("suma z1 + z2 = ")
suma1= z1.sumar(z2)
print("suma z3 + z4 = ")
suma2= z3.sumar(z4)

print("ahora trabajaremos sobre la resta con dos ejemplos")
print("resta z1 - z2 = ")
suma1= z1.restar(z2)
print("resta z3 - z4 = ")
suma2= z3.restar(z4)

print("ahora trabajaremos sobre la norma con dos ejemplos")
print("la norma de z1 es = ")
suma1= z1.norma()
print("la norma de z2 es =")
suma2= z2.norma()

print("ahora trabajaremos sobre el producto con dos ejemplos")
print("producto z1 * z2 = ")
suma1= z1.producto(z2)
print("resta z3 * z4 = ")
suma2= z3.producto(z4)

print("ahora trabajaremos sobre la división con dos ejemplos")
print("producto z1 / z2 = ")
suma1= z1.division(z2)
print("resta z3 / z4 = ")
suma2= z3.division(z4)