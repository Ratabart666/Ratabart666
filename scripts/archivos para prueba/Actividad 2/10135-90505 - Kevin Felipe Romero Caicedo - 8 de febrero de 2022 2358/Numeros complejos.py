# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Cat():
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
    def get_color(self):
        return self.color
#class instances
felix=Cat("ginger", 4 )
rover= Cat("dog-colored", 4)
stumpy= Cat("brown", 3)

print(felix.color)

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    def saludo(self):
        print(f"Bienvenido sr. {self.nombre} {self.apellido}")
#class instances
p1= Persona("John", "Cabrera")
print(p1.nombre)
print( p1.apellido)
p1.saludo()

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def edad(self):
        print(f"La edad y nombre de la persona es: . {self.name} {self.age}")
#class instances
p2= Person("Eduardo", "19")
print(p2.name)
print(p2.age)
p2.edad

class Complejos:
    def __init__(self,re, im):
        self.re=re
        self.im=im
    def suma(self, oth):
        ansre= self.re+oth.re
        ansim= self.im+oth.im
        return ansre, ansim
    def resta(self,oth):
        ansre1= self.re-oth.re
        ansim1= self.im-oth.im
        return ansre1, ansim1
    def multi(self,oth):
        
        re_re= self.re*oth.re
        re_im =self.re*oth.im
        im_re = self.im *oth.re
        im_im= self.im*oth.im
        sumita= re_im+im_re
        sumita2= (re_re+(-(im_im)))
        ansim2= sumita2, sumita
        return ansim2
    def divi(self,oth,*arg):
        divi1= ((self.re*oth.re)+(self.im*oth.im))/((oth.re**2)+(oth.im**2))
        divi2= ((self.im*oth.re)-(self.re*oth.im))/((oth.re**2)+(oth.im**2))
        return f"{divi1}+{divi2}i"

#suma_instances 1
z1=Complejos(1,2)
z2=Complejos(2,3)
print(z1.suma(z2))
#suma_instances_2
z1=Complejos(4,3)
z2=Complejos(12,4)
print(z1.suma(z2))


#resta_instances1
x1=Complejos(2,4)
x2= Complejos(4,8)
x21=print (x1.resta(x2))
#resta_instances2
x1=Complejos(3,2)
x2= Complejos(2,6)
x21=print (x1.resta(x2))

#multiplicacion_instances1
y1= Complejos(8,2)
y2= Complejos (5,3)
print (y1.multi(y2))
#multiplicacion_instances#2
y1= Complejos(12,5)
y2= Complejos (3,5)
print (y1.multi(y2))


#division_instances1
z1= Complejos( 8,6)
z2= Complejos(2,5)
print (z1.divi(z2))
#division_instances2
z1= Complejos( 4,3)
z2= Complejos(6,8)
print (z1.divi(z2))


        
        