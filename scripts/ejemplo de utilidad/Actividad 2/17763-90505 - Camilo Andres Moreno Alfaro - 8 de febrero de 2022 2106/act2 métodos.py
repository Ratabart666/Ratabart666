#Complex class - Camilo Moreno: 202021598

class compleja: #Trata a los complejos como una tupla: (Parte real, Parte imaginaria)
    def __init__ (self, Re, Im): 
        self.Im = Im
        self.Re = Re
    def suma (self, other): #suma dos complejos
        RespRe = self.Re + other.Re
        RespIm = self.Im + other.Im
        return compleja(RespRe, RespIm)
    
    def resta (self, other): #resta dos complejos
        RespRe = self.Re - other.Re
        RespIm = self.Im - other.Im
        return compleja(RespRe, RespIm)
    
    def multiplicacion (self, other): #nmultiplica dos complejos
        
        RespRe = (self.Re*other.Re - self.Im*other.Im)
        RespIm = (self.Re*other.Im + self.Im*other.Re)
        
        return compleja(RespRe, RespIm)
    
    def division (self, other): # divide un complejo entre un complejo other
        RespRe = (self.Re*other.Re + self.Im*other.Im)/(other.Re**2 + other.Im**2)
        RespIm = (self.Im*other.Re - self.Re*other.Im)/(other.Re**2 + other.Im**2)
        return compleja(RespRe, RespIm)
    
    def norma (self):
        return (self.Re**2 + self.Im**2)**(1/2)
    
    def imprimir (self): #Toma un complejo y retorna una string en forma a+bi
        if self.Im < 0:
            return str(self.Re) + " - " + str(abs(self.Im)) + "i"
        else:
            return str(self.Re) + " + " + str(self.Im) + "i"
        
# A continuación se definen 4 complejos que se usarán en los ejemplos
# Para ver los ejemplos, simplemente ejecutar el código y todo se imprime en la consola
z1 = compleja(5,12)
z2 = compleja(7,8)
z3 = compleja(4,1/2)
z4 = compleja(20, -21)

print("Ejemplos suma:")
print(f"({z1.imprimir()}) + ({z2.imprimir()}) = {z1.suma(z2).imprimir()}")
print(f"({z3.imprimir()}) + ({z4.imprimir()}) = {z3.suma(z4).imprimir()}")
print("")
print("Ejemplos resta:")
print(f"({z1.imprimir()}) - ({z2.imprimir()}) = {z1.resta(z2).imprimir()}")
print(f"({z3.imprimir()}) - ({z4.imprimir()}) = {z3.resta(z4).imprimir()}")
print(" ")
print("Ejemplos multiplicacion:")
print(f"({z1.imprimir()})({z2.imprimir()}) = {z1.multiplicacion(z2).imprimir()}")
print(f"({z3.imprimir()})({z4.imprimir()}) = {z3.multiplicacion(z4).imprimir()}")
print("")
print("Ejemplos cociente:")
print(f"({z1.imprimir()})/({z2.imprimir()}) = {z1.division(z2).imprimir()}")
print(f"({z3.imprimir()})/({z4.imprimir()}) = {z3.division(z4).imprimir()}")
print("")
print("Ejemplos norma")
print(f"|{z1.imprimir()}| = {z1.norma()}")
print(f"|{z4.imprimir()}| = {z4.norma()}")