#Clase que define los números complejos
class numero_complejo:
    #Iniciador, tiene 2 atributos, el coeficiente real y el coeficiente imaginario.
    def __init__(self,real,imaginario):
        self.real = float(real)
        self.imaginario = float(imaginario)
    #Getters atributos
    def get_real(self):
        return self.real
    def get_imaginario(self):
        return self.imaginario
    #Impresión de complejos
    def imprimir(complejo):
        signo="+"
        if(complejo.imaginario<0):
            signo=""
        print(f"{complejo.real}{signo}{complejo.imaginario}i")
    #Suma, este método toma dos números complejos(objeto),desde el que se ejecuta y uno adicional, y retorna el número complejo (objeto) resultado de sumar los entregados.
    def suma_complejo(self,sumando2):
        suma_real= self.get_real() + sumando2.get_real()
        suma_imaginarios = self.get_imaginario() + sumando2.get_imaginario()
        resultado = numero_complejo(suma_real,suma_imaginarios)
        return resultado
    #Resta, este método toma dos números complejos (objeto), restando el sustraendo (entregado por parámetro) del minuendo(número desde el que se ejecuta el metodo), y retorna el número complejo (objeto) resultado de restar los entregados.
    def resta_complejos(self, sustraendo):
        resta_real=self.get_real() - sustraendo.get_real()
        resta_imaginarios = self.get_imaginario() - sustraendo.get_imaginario()
        resultado = numero_complejo(resta_real,resta_imaginarios)
        return resultado
    #Producto, este método toma dos números complejos(objeto),desde el que se ejecuta y uno adicional, y retorna el número complejo (objeto) resultado del multiplicar los entregados.
    def producto_complejos(self, producto):
        p_real= (self.get_real()*producto.get_real())-(self.get_imaginario()*producto.get_imaginario())
        p_imaginaria =(self.get_real()*producto.get_imaginario())+(self.get_imaginario()*producto.get_real())
        resultado = numero_complejo(p_real,p_imaginaria)
        return resultado
    #Conjugado, este método toma el mismo numero desde que se ejecuta como parametro y retorna el conjugado del numero complejo.
    def conjugado(self):
        p_real=self.get_real()
        p_imaginaria=(-1)*self.get_imaginario()
        resultado = numero_complejo(p_real,p_imaginaria)
        return resultado
    #Dividir, este método toma dos números complejos(objeto),desde el que se ejecuta (Dividendo) y uno adicional(entregado por parámetro, divisor), y retorna el número complejo (objeto) resultado del divir los entregados.
    def division_complejos(self,divisor):
        div=(divisor.get_real()**2)+(divisor.get_imaginario()**2)
        p_real=((self.get_real()*divisor.get_real())+(self.get_imaginario()*divisor.get_imaginario()))/div
        p_imaginaria=((self.get_real()*divisor.get_imaginario())-(self.get_imaginario()*divisor.get_real()))/div
        resultado = numero_complejo(p_real,p_imaginaria)
        return resultado   
    #Norma, este método toma un número complejo(objeto, desde el que se ejecuta) y entrega su norma(float).
    # ||z||=sqrt(z*conjugado(z))
    def norma(self):
        conjugado=self.conjugado()
        producto= self.producto_complejos(conjugado)
        suma=(producto.get_real())+(producto.get_imaginario())
        norma=suma**(1/2)
        return norma
    
#Defino los números a trabajar
z_1=numero_complejo(2,-7) #2-7i
z_2=numero_complejo(14,19) #14+19i
z_3=numero_complejo(26/3,-11) #26-11i
z_4=numero_complejo(12,17) #12+17i
#Llevo a cabo la operaciones, imprimiento con el método imprimir el número calculado.
#Suma
print("Suma:")
zc_1 = z_1.suma_complejo(z_3)
zc_1.imprimir()
zc_2 = z_2.suma_complejo(z_4)
zc_2.imprimir()
#Resta
print("Resta:")
zc_3 = z_1.resta_complejos(z_2)
zc_3.imprimir()
zc_4 = z_1.resta_complejos(z_1)
zc_4.imprimir()
#Producto
print("Producto:")
zc_5 = z_2.producto_complejos(z_3)
zc_5.imprimir()
zc_6 = z_1.producto_complejos(z_4)
zc_6.imprimir()
#Cociente
print("Cociente:")
zc_7 = z_1.division_complejos(z_3)
zc_7.imprimir()
zc_8 = z_3.division_complejos(z_1)
zc_8.imprimir()
#Conjugado
print("Conjugado:")
zcon_1=z_1.conjugado()
zcon_1.imprimir()
zcon_3=z_3.conjugado()
zcon_3.imprimir()
#Norma de los números
print("Calculo Norma:")
norma4=f"La norma del número z_4: {z_4.get_real()}+{z_4.get_imaginario()}i, es igual a {z_4.norma()}"
print(norma4)
norma2=f"La norma del número z_2: {z_2.get_real()}+{z_2.get_imaginario()}i, es igual a {z_2.norma()}"
print(norma2)