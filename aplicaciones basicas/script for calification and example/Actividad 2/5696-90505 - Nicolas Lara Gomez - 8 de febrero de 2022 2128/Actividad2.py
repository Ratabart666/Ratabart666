
class complejos:
 
#Este es el constructor gracias al cual se van a crear los números complejos. Recibe como parámetros la parte real 
#e imaginaria de mi número.
      
    def __init__(self, real, imaginaria):
        self.real=real
        self.imaginaria=imaginaria
        
#Método de suma por medio del cual se hace la adición de la parte real y de la imaginaria de un dos números complejos.
        
    def suma(self, other):
        r = self.real + other.real
        i = self.imaginaria + other.imaginaria      
        return (r,i)
    
#Método de suma por medio del cual se hace la resta de la parte real y de la imaginaria de un dos números complejos.
    
    def resta(self, other):
        r = self.real - other.real
        i = self.imaginaria - other.imaginaria        
        return (r,i)
    
#Método del producto por medio del cual se aplica la ley distributiva y se obtiene la multiplicación de dos números 
    
    def producto(self, other):
        r = self.real*other.real - self.imaginaria*other.imaginaria
        i = self.imaginaria*other.real + self.real*other.imaginaria
        return (r,i)
    
#Método del cociente que da como resultado la división de dos números complejos.
    
    def cociente(self, other):
        r = ((self.real*other.real + self.imaginaria*other.imaginaria)/(other.real**2 + other.imaginaria**2))
        i = ((self.imaginaria*other.real - self.real*other.imaginaria)/(other.real**2 + other.imaginaria**2))
        return (r,i)
    
#Método de norma que da como resultado la norma de un número complejo.
        
    def norma(self):
        n1 = (self.real**2 + self.imaginaria**2)**(1/2)
        return n1
    
#Método de imprimir que da idea de cómo se escribiría un número complejo en la vida real.
    
    def imprimir(self):
        print(f"{self.real} + {self.imaginaria}i")
        
###Prueba Suma
        
z1 = complejos(3,7) 
z2 = complejos(9,12) 

z1_1 = complejos(10,7) 
z2_2 = complejos(-4,18) 

#print(z1.suma(z2))       #Quitar el # para hacer las pruebas correspondientes
#print(z1_1.suma(z2_2))

###Prueba Resta

z3 = complejos(20, 13)
z4 = complejos(30,5)

z3_3 = complejos(564, 29)
z4_4 = complejos(354, -13)

#print(z3.resta(z4))       #Quitar el # para hacer las pruebas correspondientes
#print(z3_3.resta(z4_4))

###Prueba Producto

z5 = complejos(5, 2)
z6 = complejos(3,-4)

z5_5 = complejos(10, 5)
z6_6 = complejos(33,-5)

#print(z5.producto(z6))       #Quitar el # para hacer las pruebas correspondientes
#print(z5_5.producto(z6_6)) 

###Prueba Cociente

z7 = complejos(5,-3)
z8 = complejos(2,1)

z7_7 = complejos(1,-3)
z8_8 = complejos(19,6)

#print(z7.cociente(z8))       #Quitar el # para hacer las pruebas correspondientes
#print(z7_7.cociente(z8_8))

###Prueba norma

z9 = complejos(3,4)
z9_9 = complejos(6,6)

#print(z9.norma())       #Quitar el # para hacer las pruebas correspondientes
#print(z9_9.norma())

#z9.imprimir()
#z9_9.imprimir()
        