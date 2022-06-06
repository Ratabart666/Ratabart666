#Gerson Ponce
class Complejo:
    #se crea la clase Complejo para definir los métodos
    def __init__(self, real, imaginaria):
        #Constructor de la clase Complejo, se define la parte real y la imaginaria de cada numero complejo a partir de los parametros
        self.real = real
        self.imaginaria = imaginaria

    def suma(self, complejo):
   #Suma, se suman los valores reales de 2 números complejos y luego se suma la parte imaginaria de los 2 y por ultimo se devuelve un objeto de la clase Complejo con los valores de la suma realizada
        nuevo_real = self.real + complejo.real
        nuevo_imag = self.imaginaria + complejo.imaginaria
        return Complejo(nuevo_real, nuevo_imag)

    def resta(self, complejo):
        #Resta, la misma teoría que la suma, solo que restando
        nuevo_real = self.real - complejo.real
        nuevo_imag = self.imaginaria - complejo.imaginaria
        return Complejo(nuevo_real, nuevo_imag)

    def multiplicacion(self, complejo):
        #Multiplicación, en la parte real se multiplica la parte real de cada número y se resta con la multiplicación del número de la parte imaginaria, haciendo lo contrario en el imaginario
        nuevo_real = self.real*complejo.real - self.imaginaria*complejo.imaginaria
        nuevo_imag = self.real*complejo.imaginaria + self.imaginaria*complejo.real
        return Complejo(nuevo_real, nuevo_imag) 
    
    def division(self, complejo):
        #División, la división tiene algo especial en cuanto a las otras operaciones, y es que primero se calcula el divisor para hacer el código más eficiente, o fácil de entender, el divisor se calcula como la parte real del segundo número al cuadrado sumado con la parte imaginaria del mismo número al cuadrado, a continuación la parte real se calcula como la parte real de los numeros multiplicada y luego sumada con la multiplicacion de la parte imaginaria, dividiendo todo esto entre el divisor, cambiando el signo a menos en el caso de imaginario, luego se retorna un objeto Complejo con estos valores
        divisor = (complejo.real ** 2) + (complejo.imaginaria ** 2)
        nuevo_real = (self.real*complejo.real + self.imaginaria*complejo.imaginaria) / divisor
        nuevo_imag = (self.imaginaria*complejo.real - self.real*complejo.imaginaria) / divisor
        return Complejo(nuevo_real, nuevo_imag)


# PRUEBAS
#Pruebas suma
complejo1 = Complejo(2, 7)
complejo2 = Complejo(3, -4)
complejosuma = complejo1.suma(complejo2)
print(complejosuma.real, complejosuma.imaginaria)

complejo3 = Complejo(3, 7)
complejo4 = Complejo(4, -4)
complejosuma1 = complejo3.suma(complejo4)
print(complejosuma1.real, complejosuma1.imaginaria)

#Pruebas resta
rcomplejo1 = Complejo(9, 5)
rcomplejo2 = Complejo(4, 7)
complejoresta = rcomplejo1.resta(rcomplejo2)
print(complejoresta.real, complejoresta.imaginaria)

rcomplejo3 = Complejo(8, 5)
rcomplejo4 = Complejo(3, 7)
complejoresta1 = rcomplejo3.resta(rcomplejo4)
print(complejoresta1.real, complejoresta1.imaginaria)

#Pruebas multiplicación
mcomplejo1 = Complejo(3, 2)
mcomplejo2 = Complejo(5, 6)
complejom = mcomplejo1.multiplicacion(mcomplejo2)
print(complejom.real, complejom.imaginaria)

mcomplejo3 = Complejo(4, 2)
mcomplejo4 = Complejo(6, 6)
complejom1 = mcomplejo3.multiplicacion(mcomplejo4)
print(complejom1.real, complejom1.imaginaria)

#Pruebas cociente/división
dcomplejo1 = Complejo(3, 2)
dcomplejo2 = Complejo(4, -5)
complejod = dcomplejo1.division(dcomplejo2)
print(complejod.real, complejod.imaginaria)

dcomplejo3 = Complejo(4, 2)
dcomplejo4 = Complejo(5, -5)
complejod1 = dcomplejo3.division(dcomplejo4)
print(complejod1.real, complejod1.imaginaria)

#Pruebas norma
complejo = Complejo(1/(2**(1/2)), 1/(2**(1/2)))
norma = complejo.norma()
print(norma)

complejo = Complejo(3,4)
norma1 = complejo.norma()
print(norma1)

