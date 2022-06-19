class complejos:
    def __init__ (self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria
        
    def suma (self, other):
        pr = self.real + other.real
        pi = self.imaginaria + other.imaginaria
        res = f"{pr} + {pi}i"
        return res
    #La función toma la parte real de un númeor y lo suma con la aparte real del otro.
    #También toma la parte imaginaria de uno y la suma con la imaginaria del otro
    
    def resta (self, other):
        pr = self.real - other.real
        pi = self.imaginaria - other.imaginaria
        res = f"({pr}) + ({pi})i"
        return res
    #La función toma la parte real de un númeor y lo resta con la aparte real del otro.
    #También toma la parte imaginaria de uno y la resta con la imaginaria del otro
    
    def producto (self,other):
        a = self.real * other.real
        b = self.real * other.imaginaria
        c = self.imaginaria * other.real
        d = self.imaginaria * other.imaginaria
        #Primero se hacen los productos por la propiedad distributiva
        D = -d
        #se altera el signo del número con producto de dos factores imaginarios
        real = a + D
        im = b + c
        res = f"{real} + {im}i"
        #se retornan los valores reales e imaginarios por aparte
        return res   
    
    def apoyo1 (self,other):
        #la función obtendrá los productos por separado de la parte real e imaginaria y las acumulará en listas para que sean más fáciles de manipular en la siguiente función.
        a = self.real * other.real
        b = self.real * other.imaginaria
        c = self.imaginaria * other.real
        d = self.imaginaria * other.imaginaria
        #Primero se hacen los productos por la propiedad distributiva
        D = -d
        #se altera el signo del número con producto de dos factores imaginarios
        real = a + D
        im = b + c
        res = [real,im]
        #se retornan los valores reales e imaginarios por aparte
        return res 
    
    def cociente (self,other):
        #la función dividirá el primer número entre el segundo número e invocará a la función de producto para facilitar las cosas.
        inverso = other.imaginaria * -1
        nother = complejos(other.real,inverso)
        n = complejos.apoyo1(self,nother)
        d = complejos.apoyo1(other,nother)
        rnum = (n[0])
        inum = (n[1])
        r1 = rnum/d[0]
        r2= inum/d[0]
        res = f"{r1} + {r2}i"
        return res
    
    def norma (self):
        norma = ((self.real)**2) + ((self.imaginaria)**2)**(1/2)
        return norma
        
        
    
a1 = complejos(1,2)
a2 = complejos(3,4)
a3 = complejos(1,-2)
a4 = complejos(3,5)


x = complejos.suma(a1,a2)
x1 = complejos.suma(a3,a4)

y = complejos.resta(a1,a2)
y1 = complejos.resta(a3,a4)

z = complejos.resta(a1,a2)
z1 = complejos.resta(a3,a4)

p = complejos.producto(a1,a2)
p1 = complejos.producto(a3,a4)

q = complejos.cociente(a1,a2)
q1 = complejos.cociente(a3,a4)

r = complejos.norma(a1)
r1 = complejos.norma(a2)

print (f"La suma de a1 y a2 es {x}")
print (f"La suma de a3 y a4 es {x1}")

print (f"La resta de a1 y a2 es {y}")
print (f"La resta de a3 y a4 es {y1}")

print (f"El producto de a1 y a2 es {z}")
print (f"El producto de a3 y a4 es {z1}")

print (f"El cociente de a1 y a2 es {q}")
print (f"El cociente de a3 y a4 es {q1}")

print (f"La norma de a1 es {r}")
print (f"La norma de a2 es {r1}")