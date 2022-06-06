#Estimados estudiantes,

#Para la actividad se recomienda leer previamente, según la disponibilidad de tiempo, la diferencia entre arrays, listas y diccionarios en python así como leer sobre
#clases en python.

#1. Crear una clase en la que se definan las operaciones para los números complejos, esto es: la suma, la resta, el producto, el cociente y la norma de dos números complejos.
#2. Mostrar los resultados de las operaciones con dos ejemplos para cada operación.
#Nota: Recuerden que todos los códigos enviados deben estar comentados.

#Entregables: archivo .py 

#Criterios de evaluación:
#1. 25 puntos # 5 por cada operación realizada
#2. 25 puntos # 5 por cada operación realizada#

class compleja: #Se crea la clase
    def __init__(self, Re, Im): #Se definene las instancias
        self.Re=Re
        self.Im=Im
    def suma(self,other): #Función de suma para numeros complejos
        r = self.Re+other.Re
        i = self.Im+other.Im
        return str(r) + "+" + "(" + str(i) + ")i"
    def resta(self,other): #Función de resta para numeros complejos
        r = self.Re-other.Re
        i = self.Im-other.Im
        return str(r) + "+" + "(" + str(i) + ")i"
    def producto(self,other): #Función de producto para numeros complejos
        r = (self.Re*other.Re)-(self.Im*other.Im)
        i = (self.Re*other.Im)+(self.Im*other.Re)
        return str(r) + "+" + "(" + str(i) + ")i"
    def cociente(self,other): #Función de cociente para numeros complejos
        r = round(((self.Re*other.Re)+(self.Im*other.Im))/(other.Re**2+other.Im**2),2)
        i = round(((self.Im*other.Re)-(self.Re*other.Im))/(other.Re**2+other.Im**2),2)
        return str(r) + "+" + "(" + str(i) + ")i"
    def norma(self,other): #Función para hallar la norma de numeros complejos
        r=((self.Re**2)+(self.Im**2))**(1/2)
        i=((other.Re**2)+(other.Im**2))**(1/2)
        return round(r, 2), round(i,2)
z1=compleja(1,2)
z2=compleja(3,4)
z3=compleja(5,6)
z4=compleja(7,8)
print("Suma")
print(z1.suma(z2))
print(z3.suma(z4))
print("Resta")
print(z1.resta(z2))
print(z2.resta(z4))
print("Producto")
print(z1.producto(z2))
print(z3.producto(z4))
print("Cociente")
print(z1.cociente(z2))
print(z3.cociente(z4))
print("Norma")
print(z1.norma(z2))
print(z3.norma(z4))