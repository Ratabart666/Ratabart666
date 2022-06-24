# Definimos clase Numeros_Complejos
class Numeros_Complejos:
    def __init__(self,num_1,num_2):
        self.complejo_1 = num_1
        self.complejo_2 = num_2
        
        #Suma
        self.suma = self.complejo_1 + self.complejo_2
        
        
        #Resta
        self.resta = self.complejo_1 - self.complejo_2
        
        
        #Producto
        self.producto = self.complejo_1 * self.complejo_2
        
        
        #Cociente 
        self.cociente = self.complejo_1 / self.complejo_2
            
        
        #La Norma
        self.norma_1 = abs(self.complejo_1)
        
        self.norma_2 = abs(self.complejo_2)
    
        
#Ejemplos para la class Numeros_complejos

pareja_1 = Numeros_Complejos(4+2j, 2+3j)
pareja_2 = Numeros_Complejos(3+2j, 6+3j)

#Se imprimen los ejemplos de cada una de las operaciones para pareja_1
print ("La suma de los numeros complejos para la pareja_1 es: ", pareja_1.suma)
print ("La resta de los numeros complejos para la pareja_1 es: ", pareja_1.resta)
print ("El producto de los numeros complejos para la pareja_1 es: ", pareja_1.producto)
print ("El cociente de los numeros complejos para la pareja_1 es: ", pareja_1.cociente) 
print ("La Norma de numero complejo 1 es: ", pareja_1.norma_1)
print ("La Norma del numero complejo 2 es: ", pareja_1.norma_2, "\n")  

#Se imprimen los ejemplos de cada una de las operaciones para pareja_2
print ("La suma de los numeros complejos para la pareja_2 es: ", pareja_2.suma)
print ("La resta de los numeros complejos para la pareja_2 es: ", pareja_2.resta)
print ("El producto de los numeros complejos para la pareja_2 es: ", pareja_2.producto)
print ("El cociente de los numeros complejos para la pareja_2 es: ", pareja_2.cociente) 
print ("La Norma del numero complejo 1 es: ", pareja_2.norma_1)
print ("La Norma del numero complejo 2 es: ", pareja_2.norma_2)  
