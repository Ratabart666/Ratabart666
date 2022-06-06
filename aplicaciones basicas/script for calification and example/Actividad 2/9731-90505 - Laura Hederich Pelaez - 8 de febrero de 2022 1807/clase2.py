#Clase que define las operaciones para los números complejos donde se entra una parte real y una parte imaginaria para cada
#uno de los dos números de tal forma que: 
#a = parte real primer número b = parte imaginaria primer numero 
#c = parte real segund numero y d = parte imaginaria segundo numero 

class complejos: 

    #Método que inicia los atributos. Donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Ver ejemplo al final de la clase. 
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    #Método que suma dos los números complejos formados por los parámetros a, b, c y d donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Devuelve la suma entre a + bi y c + di
    def suma (a, b, c, d): 
        c1 = complex(a, b)
        c2 = complex(c, d)
        s = c1 + c2

        return s

    #Método que resta los dos números complejos formados por los parámetros a, b, c y d donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Devuelve la resta entre a + bi y c + di
    def resta(a, b, c, d): 
        c1 = complex(a, b)
        c2 = complex(c, d)
        r = c1 - c2

        return r

    #Método que multiplica números complejos formados por los parámetros a, b, c y d donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Devuelve la multiplicación entre a + bi y c + di. 
    def multiplicacion(a, b, c, d): 
        c1 = complex(a, b)
        c2 = complex(c, d)
        m = c1 * c2

        return m

    #Método que multiplica números complejos formados por los parámetros a, b, c y d donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Devuelve el concientre entre a + bi y c + di
    def cociente(a, b, c, d): 
        c1 = complex(a, b)
        c2 = complex(c, d)
        d = c1 / c2

        return d

    #Método que devuelve la norma de un número complejo donde a es la parte real del primer número, b es la parte imaginaria del primer numero 
    #c es la parte real del segundo numero y d es la parte imaginaria del segundo numero. 
    #Devuelve la norma de a + bi
    def norma(a, b):    
        r = ((a**2)+(b**2))**(1/2)
        
        return r
        

##EJEMPLO 1       

a = 1 #Parte real del número 1
b = 4 #Parte imaginaria del número 1
#En consecuencia el número 1 para esta prueba sería 1 + 4j

c = 5 #Parte real del número 2
d = 6 #Parte imaginaria del número 2
#En consecuenica el número 2 para esta prueba sería 5 + 6j 

complejos.suma(a, b, c, d)
complejos.resta(a, b, c, d)
complejos.multiplicacion(a, b, c, d)
complejos.cociente(a, b, c, d)
complejos.norma(a, b)

##EJEMPLO 2
e = -1 #Parte real del número 1
f = 6 #Parte imaginaria del número 1
#En consecuencia el número 1 para esta prueba sería -1 + 6j

g = 10 #Parte real del número 2
h = -8 #Parte imaginaria del número 2
#En consecuenica el número 2 para esta prueba sería 10 - 8j 

complejos.suma(e, f, g, h)
complejos.resta(e, f, g, h)
complejos.multiplicacion(e, f, g, h)
complejos.cociente(e, f, g, h)
complejos.norma(e, f)