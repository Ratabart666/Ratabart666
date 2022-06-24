# Creamos la clase:
from typing_extensions import Self


class compleja:
  # Establecemos la componente real e imaginaria:
  def __init__(self, re, im):
    self.re = re
    self.im = im
  # Programamos la operacion de suma: 
  def suma(self, other):
    return ((self.re + other.re, self.im + other.im))
  # Programamos la operacion de resta: 
  def resta(self, other):
    return (self.re - other.re, self.im - other.im)
  # Programamos la operacion de producto: 
  def producto(self, other):
    return ((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))
  # Programamos la operacion de cociente: 
  def cociente(self, other):
    return (((self.re * other.re + self.im * other.im)/(other.re**2 + other.im**2)), ((self.im * other.re - self.re * other.im)/(other.re**2 + other.im**2)))
  # Programamos la operacion de norma:
  def norma(self):
    return ((self.re**2 + self.im**2)**(1/2))

# Aqui declaramos que las variables z1, z2, z3 y z4 y las igualamos a nuestra clase con sus valores respectivos:
z1 = compleja(0, 2) 

z2 = compleja(2, 3)

z3 = compleja(11, 4) 

z4 = compleja(5, 6) 

# Aqui probamos nuestras operaciones, el resultado saldra en forma de vector; (a, b), siendo a la componente real y b
# la componente imaginaria respectivamente (excepto la norma): 

print(f"Suma #1: {z1. suma(z2)}")

print(f"Resta #1: {z1. resta(z2)}")

print(f"Producto #1: {z1. producto(z2)}")

print(f"Cociente #1: {z1.cociente(z2)}")

print(f"Norma #1: {z1.norma()}")

print(f"Suma #2: {z3.suma(z4)}")

print(f"Resta #2: {z3.resta(z4)}")

print(f"Producto #2: {z3.producto(z4)}")

print(f"Cociente #2: {z3.cociente(z4)}")

print(f"Norma #2: {z3.norma()}")





