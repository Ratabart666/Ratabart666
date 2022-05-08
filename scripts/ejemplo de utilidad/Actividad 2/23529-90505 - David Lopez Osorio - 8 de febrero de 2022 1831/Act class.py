# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:21:38 2022

@author: dlope
"""

class Complejos:
    def __init__ (self,Re,Im):
        self.Im = Im
        self.Re = Re

#Re se refiere al aspecto real del numero y el Im al imaginario
#Para sumar tomamos los atributos .Re y .Im por separado (real con real e imaginario con imaginario), los sumamos, y formamos un complejo con los resultados
    def suma (self,number):
        r = self.Re + number.Re
        i = self.Im + number.Im
        return Complejos(r,i).imprimir()

#Para restar tomamos los atributos .Re y .Im por separado (real con real e imaginario con imaginario), los restamos, y formamos un complejo con los resultados    
    def resta (self,number):
        r = self.Re - number.Re
        i = self.Im -number.Im
        return Complejos(r,i).imprimir()

#Para el producto aplicamos el proceso necesario para obtener la parte real e imaginaria por separado, llamando los atributos adecuados, y luego lo juntamos en un complejo    
    def producto (self,number):
        r = (self.Re*number.Re)-(self.Im*number.Im)
        i = (self.Re*number.Im)+(self.Im*number.Re)
        return Complejos(r,i).imprimir()

#Para el cociente se generó una variable con el divisor para no repetirlo innecesariamente, luego aplicamos el proceso necesario para obtener la parte real e imaginaria por separado, llamando los atributos adecuados, y finalmente lo juntamos en un complejo    
    def cociente (self,number):
        div = (number.Re**2)+(number.Im**2)
        r = ((self.Re*number.Re)+(self.Im*number.Im))/div
        i = ((self.Im*number.Re)-(self.Re*number.Im))/div
        return Complejos(r,i).imprimir()
    
#Para la norma llamamos a los atributos necesarios y aplicamos la formula
    def norma (self):
        ans = (self.Re**2+self.Im**2)**(1/2)
        return ans
    
#Esta función convierte los Complejos en strings legibles    
    def imprimir (self):
        return str(self.Re)+"+"+str(self.Im)+"i"
    

z1 = Complejos(1,2)
z2 = Complejos(2,3)
z3 = Complejos(1,1)
z4 = Complejos(4,2)

print(z1.suma(z2))
print(z3.suma(z4))
print(z1.resta(z2))
print(z3.resta(z4))
print(z1.producto(z2))
print(z3.producto(z4))
print(z1.cociente(z2))
print(z3.cociente(z4))
print(z1.norma())
print(z2.norma())




        