
import numpy as np

class complejo:
    #se procede a realizar el contructor:
    
    def __init__(self, Re, Im):
        self.Re=Re #parte real
        self.Im=Im #parte imaginaria
    
    #se procede a definir las operaciones en la clase->complejo
    
    #definicion de la suma
    def suma(self,otro):
        
        a= self.Re + otro.Re #suma de la parte real
        b= self.Im + otro.Im #suma de la parte imaginaria
        
        a= round(a,3) 
        b= round(b,3)
        
        return [(a,b) , f"{a} + ({b})i"]
    
    #definicion de la resta
    def resta(self,otro):
        
        a= self.Re - otro.Re #diferencia de la parte real
        b= self.Im - otro.Im #diferenecia de la parte imaginaria
        
        a= round(a,3)
        b= round(b,3)
        
        return [(a,b) , f"{a} + ({b})i"]
    
    #definicion del producto
    def producto(self,otro):
        
        a= ( ((self.Re)*(otro.Re))-( (self.Im)*(otro.Im) ) ) #producto de la parte real
        b= ( ((self.Re)*(otro.Im))+( (self.Im)*(otro.Re) ) ) #procucto de parte imaginaria
        
        a= round(a,3)
        b= round(b,3)
        
        return [(a,b) , f"{a} + ({b})i"]
    
    #definicion del producto
    def division(self,otro):
        
        a=  ( ((self.Re)*(otro.Re))+( (self.Im)*(otro.Im) ))/( (otro.Re)**2 + (otro.Im)**2 ) #division de la parte real
        b= ( ((self.Im)*(otro.Re)) - ((self.Re)*(otro.Im)) )/( (otro.Re)**2 + (otro.Im)**2 ) #division de la parte imaginaria
        
        a= round(a,3)
        b= round(b,3)
        
        return [(a,b) , f"{a} + ({b})i"]
    
    #definicion de la norma
    def norma(self):
        
        norma = (( (self.Re)**2 )+ ( (self.Im)**2 ))**(1/2) #modulo del numero imaginario
        
        norma= round(norma,3)
        
        return norma
    
    #definicion del conjugado
    def conjugado(self):
        
        a= self.Re
        b= -self.Im
        
        return [(a,b) , f"{a} + ({b})i"]
    
    #definicion del argumento
    
    def argumento(self):
        
        arg= np.arctan( (self.Im)/(self.Re) ) #el argumento sera retornado en radianes pues numpy trabaja en radianes
        
        arg=round(arg,3)
        
        return arg
    
#ejemplos

z1= complejo(1,2)
z2= complejo(3,4)
z3=complejo(5,6)
z4=complejo(7,8)

#suma
print("suma")
print(complejo.suma(z1,z2))
print(complejo.suma(z3,z4))

#resta
print("resta")
print(complejo.resta(z1,z2))
print(complejo.resta(z3,z4))

#producto
print("producto")
print(complejo.producto(z1,z2))
print(complejo.producto(z3,z4))

#division
print("division")
print(complejo.division(z1,z2))
print(complejo.division(z3,z4))

#norma
print("norma")
print(complejo.norma(z1))
print(complejo.norma(z2))

#conjugado
print("conjugado")
print(complejo.conjugado(z1))
print(complejo.conjugado(z2))

#argumento
print("argumento")
print(complejo.argumento(z1))
print(complejo.argumento(z2))

"""    
referencias:
    
Demostraciones de las propiedades básicas de los números complejos o imaginarios. (2022). Matesfacil.com.
https://www.matesfacil.com/ejercicios-resueltos-demostraciones-complejos.html

"""




