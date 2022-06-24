class complejos:
    def __init__(self, parteReal, parteImg): #metodo que inicializa los atributos de las partes real e imaginaria del numero complejo
        self.parteReal = parteReal
        self.parteImg = parteImg

    def suma(self, other): #calcula la suma de dos numeros complejos dados
        sumaReal = self.parteReal + other.parteReal
        sumaImg = self.parteImg + other.parteImg
        return complejos(sumaReal, sumaImg)

    def resta(self, other): #calcula la resta de dos numeros complejos dados
        restaReal = self.parteReal - other.parteReal
        restaImg = self.parteImg - other.parteImg
        return complejos(restaReal, restaImg)

    def producto(self, other): #calcula el producto de dos numeros complejos dados
        prodReal = (self.parteReal * other.parteReal) - (self.parteImg * other.parteImg)
        prodImg = (self.parteReal * other.parteImg) + (self.parteImg * other.parteReal)
        return complejos(prodReal, prodImg)

    def cociente(self, other): #calcula el cociente entre dos numeros complejos dados
        divReal = ((self.parteReal * other.parteReal) + (self.parteImg * other.parteImg)) / (other.parteReal**2 + other.parteImg**2)
        divImg = ((self.parteImg * other.parteReal) - (self.parteReal * other.parteImg)) / (other.parteReal**2 + other.parteImg**2)
        return complejos(divReal, divImg)

    def norma(self): #calcula la norma de un numero complejo dado
        norma = ((self.parteReal)**2 + (self.parteImg)**2)**(1/2)
        return norma

    def imprimir(self): #retorna el str del numero complejo de la forma "a+bi" para el caso de b>0 y de "a-bi" para b<0
        if self.parteImg > 0:
            return f"{self.parteReal}+{self.parteImg}i"
        else:
            return f"{self.parteReal}{self.parteImg}i"

#ejemplos de prueba
z1 = complejos(1,2)
z2 = complejos(2,3)
z3 = complejos(3,5)
#suma
print(complejos.suma(z1, z2).imprimir())
print(complejos.suma(z2, z3).imprimir())
#resta
print(complejos.resta(z1, z2).imprimir())
print(complejos.resta(z2, z3).imprimir())
#producto
print(complejos.producto(z1, z2).imprimir())
print(complejos.producto(z2, z3).imprimir())
#cociente
print(complejos.cociente(z1, z2).imprimir())
print(complejos.cociente(z2, z3).imprimir())
#norma
print(complejos.norma(z1))
print(complejos.norma(z2))