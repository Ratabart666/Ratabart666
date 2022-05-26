#La clase Complejos va a contener a los numeros complejos cuyos atributos son su parte real y compleja
class Complejos:
    def __init__(self, real, imaginario):
        self.real=real
        self.imaginario=imaginario
#La suma de complejos suma literalmente las partes reales y las une con las partes complejas.
#Se acude a los atributos de cada instancia para poder acceder a cada una de las componentes real
# y compleja de cada numero. Esto aplica para cada unade las funciones abajo.
    def suma_complejos(self,complejo_2):
        suma_real=float(self.real+complejo_2.real)
        suma_imaginaria=float(self.imaginario+complejo_2.imaginario)
        print("La suma resultante es {}+{}i".format(suma_real,suma_imaginaria))
        return Complejos(suma_real,suma_imaginaria)
#La resta es casi igual que la suma, excepto que en la resta se hace una diferencia
    def resta_complejos(self,complejo_2):
        resta_real=float(self.real-complejo_2.real)
        resta_imaginaria=float(self.imaginario-complejo_2.imaginario)
        print("La resta resultante es {}+{}i".format(resta_real,resta_imaginaria))
        return Complejos(resta_real,resta_imaginaria)
#En la norma sumamos los cuadrados de las partes real y compleja del numero dado, todo sobre raiz
    def norma_complejos(self):
        n=(((self.real)**2)+((self.imaginario)**2))**(1/2)
        print("La norma es {}".format(n))
        return n
#Para el producto de complejos se sigue la formula (ac-bd)+(ad+bc)
    def producto_complejos(self,complejo_2):
        producto_1=(self.real*complejo_2.real)-(self.imaginario*complejo_2.imaginario)
        producto_2=(self.real*complejo_2.imaginario)+(self.imaginario*complejo_2.real)
        print("El producto resultante es {}+{}i".format(producto_1,producto_2))
        return Complejos(producto_1,producto_2)
#Para el cociente se sigue la formula ((ac+bs)/(c**2+d**2))+((bc-ad)/(c**2+d**2)) 
    def cociente_complejos(self,complejo_2):
        cociente_1=((self.real*complejo_2.real)+(self.imaginario*complejo_2.imaginario))/((complejo_2.real**2)+(complejo_2.imaginario**2))
        cociente_2=((self.imaginario*complejo_2.real)-(self.real*complejo_2.imaginario))/((complejo_2.real**2)+(complejo_2.imaginario**2))
        print("El cociente resultante es {}+{}i".format(cociente_1,cociente_2))
        return Complejos(cociente_1,cociente_2)
    
    def imprimir(self):
        print("{}+{}i".format(self.real,self.imaginario))

a=Complejos(1,2)
b=Complejos(1,1)
c=Complejos(0,1)
d=Complejos(1,0)
a.suma_complejos(c)
b.suma_complejos(d)
c.resta_complejos(d)
a.resta_complejos(b)
d.norma_complejos()
b.norma_complejos()
a.producto_complejos(d)
c.producto_complejos(d)
c.cociente_complejos(d)
a.cociente_complejos(b)