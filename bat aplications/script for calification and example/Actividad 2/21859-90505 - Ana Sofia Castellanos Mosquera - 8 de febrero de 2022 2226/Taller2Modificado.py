#Clase complejo: Se define la parte real e imaginaria
class Complejo:

    # Metodo constructor de un complejo (Parte real y parte imaginaria)
    def __init__ ( self, partereal:float, parteimaginaria: float):
        self.real = partereal
        self.imaginaria = parteimaginaria

    """Nota: Cada metodo retorna una tupla con un string en la primera posicion
    que indica la operacion que se realiza y un resultado de tipo Complejo, esto se hace 
    puesto que en el formato se da el tipo de operando usado y su resultado."""
    
    # Si se desea hacer con más argumentos se añade *args
    # Suma la instancia del objeto con otro complejo que ingresa por parámetro
    
    def suma (self,other):
        #Suma self(instancia) - other (por parametro)
        real = self.real + other.real 
        imaginaria = self.imaginaria + other.imaginaria
        resultado = Complejo (real, imaginaria)
        return "suma",  resultado

    # Resta la instancia del objeto con otro complejo que ingresa por parámetro
    def resta (self,other):
        #Resta self (instancia) - other( por parámetro)
        """ La resta de complejos se realiza restando la parte real de ambos números (parte real de la resta)
        y restando las partes imaginarias (parte imaginaria de la resta) """
        real = self.real - other.real 
        imaginaria = self.imaginaria - other.imaginaria
        resultado = Complejo (real, imaginaria)
        return "resta", resultado

    # Multiplica la instancia del objeto con otro complejo que ingresa por parámetro
    def multiplicacion (self,other):
        """ Considerando dos numeros complejos a+bi y c+di 
        se define el producto como (a+bi)(c+di) = ac + adi + bci+ bdi^2 
        Por definicion i^2 = -1 con lo cual se tiene que: 
        (a+bi)(c+di) = ac + adi + bci- bd
        Agrupando las partes real e imaginaria: 
        (a+bi)(c+di) = (ac - bd) + (ad + bc)i
         """
        real = ((self.real*other.real)-(self.imaginaria*other.imaginaria))
        imaginaria = ((self.real*other.imaginaria)+(self.imaginaria*other.real))

        resultado = Complejo (real, imaginaria)
        return "multiplicacion", resultado
    #Halla la norma del self (instancia)
    def norma (self):
        """Considerando un numero complejo a+bi 
        se define la norma como su distancia al origen es decir n^2 = real^2 +imaginaria^2 """
        resultado = (((self.real)**2 + (self.imaginaria)**2))**(1/2)
        return "norma", resultado
    #Halla el cociente entre self  (la intancia del objeto) y other que ingresa por parametro 
    def cociente (self,other):
        #Divide complejo1/complejo 2
        """Considerando dos numeros complejos a+bi y c+di 
        se define el cociente como (a+bi)/(c+di)= (a+bi)/(c+di) * (c-di)/(c-di)
        = ((ac - bd) + (ad + bc)i)/(c^2-(d^2*i^2)) 
        =((ac - bd) + (ad + bc)i)/(c^2 + d^2)
        =(ac + bd)/(c^2 + d^2) + (ad - bc)i/(c^2 + d^2)"""
        
        ParteRealNum = (self.real*other.real)+(self.imaginaria*other.imaginaria)
        ParteImaginariaNum = (-1*self.real*other.imaginaria)+(self.imaginaria*other.real)
        den = ((other.real)**2) + ((other.imaginaria)**2)

        real= ParteRealNum/den
        imaginario =ParteImaginariaNum/den

        resultado = Complejo (real, imaginario)
        
        return "cociente", resultado

def DarFormato (tupla):
    #Da formato de salida al resultado tomando la tupla de resultado de las operaciones
    if tupla[0] == "norma":
        print (f"El resultado de {tupla[0]} es {tupla[1]}")
    else:
        print (f"El resultado de {tupla[0]} es {tupla[1].real} + {tupla[1].imaginaria}i")

#Pruebas
#Definición de dos objetos complejos
complejo1 = Complejo(5,4)
complejo2 = Complejo(3,2)

####Operaciones####
#Suma de complejos
print(f"Ejemplo 1: operacion entre {complejo1.real} + {complejo1.imaginaria}i y {complejo2.real} + {complejo2.imaginaria}i")
suma = complejo1.suma(complejo2)
DarFormato(suma)
#Resta de complejos
sub = complejo1.resta(complejo2)
DarFormato(sub)
#Multiplicacion de complejos
mult = complejo1.multiplicacion(complejo2)
DarFormato(mult)
#Norma del complejo1
norm = complejo1.norma()
DarFormato(norm)
#Cociente de complejo1/complejo2
coci = complejo1.cociente(complejo2)
DarFormato(coci)

##Ejemplo 2##
complejo1_2 = Complejo(-7,9)
complejo2_2 = Complejo(5,-2)

####Operaciones####
#Suma de complejos
print(f"Ejemplo 2: operacion entre {complejo1_2.real} + {complejo1_2.imaginaria}i y {complejo2_2.real} + {complejo2_2.imaginaria}i")
suma = complejo1_2.suma(complejo2_2)
DarFormato(suma)
#Resta de complejos
sub = complejo1_2.resta(complejo2_2)
DarFormato(sub)
#Multiplicacion de complejos
mult = complejo1_2.multiplicacion(complejo2_2)
DarFormato(mult)
#Norma del complejo1
norm = complejo1_2.norma()
DarFormato(norm)
#Cociente de complejo1/complejo2
coci = complejo1_2.cociente(complejo2_2)
DarFormato(coci)