# -*- coding: utf-8 -*-

class complejos: 
    def __init__(self,real, imaginaria): #dos atributos: parte real e imaginaria
        self.real = real
        self.imaginaria = imaginaria
    
    def suma (self, other):
        c = self.real + other.real 
        b = self.imaginaria + other.imaginaria
        return c,b
    
    def resta (self, other):
        d = self.real - other.real
        e = self.imaginaria - other.imaginaria
        
        return d,e
    
    def multiplicación (self, other): 
        real_real = self.real * other.real
        real_imaginario = self.real * other.imaginaria
        imaginario_real = self.imaginaria * other.real
        imaginario_imaginario = self.imaginaria * other.imaginaria
        suma_termino_i = real_imaginario + imaginario_real
        numero_imaginario_imaginario = - imaginario_imaginario
        suma_real = real_real + numero_imaginario_imaginario
        
        #Todas las anteriores funciones básicamente lo que hacen es multiplicar todos los términos del número complejo; es decir, la propiedad distributiva.
        #Posteriormente se suman términos semejantes: los términos que tienen i y los reales. 
        #La función numero_imaginario_imaginario se encarga de llevar a cabo la propiedad de que i elevado al cuadrado es igual a -1. Esto convierte el número imaginario resultante de multiplicar la parte imaginaria de ambos números en uno real. 
        
        
        return suma_real, suma_termino_i
    
    def división (self, other): 
        
        ima = -(self.imaginaria*other.imaginaria)
        deno = (other.real**2) + (other.imaginaria**2)
        divi = (((self.real*other.real)+ima)/deno)+(((self.real*other.imaginaria)+(self.imaginaria*other.real)))/deno
        
        #Profe la verdad no sé en que está fallando mi código para la división, pero no me da el resultado correcto, lo intenté de varias formas y no no se en que me estoy equivocando :(
        
        return divi 

    
#Ejemplos por cada función. 

#Suma

z1 = complejos(1,2j) #1+2i
z2 = complejos (2,3j) #2+3i

z3 = complejos(4,5)
z4 = complejos(8,2)

print(z3.suma(z4))

#Resta

z1 = complejos(4,2j) 
z2 = complejos (2,6j) 

z3 = complejos(4,5)
z4 = complejos(7,2)

print(z1.resta(z2))

#Multiplicación

z1 = complejos(6,2j) 
z2 = complejos (8,1j) 

z3 = complejos(2,5)
z4 = complejos(8,4)

print(z3.multiplicación(z4))

#División

z1 = complejos(2,5j)
z2 = complejos (6,8j) 

z3 = complejos(4,5)
z4 = complejos(1,2)

print(z1.división(z2))
