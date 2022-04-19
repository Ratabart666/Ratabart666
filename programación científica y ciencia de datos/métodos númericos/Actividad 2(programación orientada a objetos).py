#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Compleja:
    def __init__(self,real,compleja):
        self.real=real
        self.compleja=compleja
    def suma(self,other):
        return((self.real+other.real,self.compleja+other.compleja))
    def resta(self,other):
        return((self.real-other.real,self.compleja-other.compleja))
    def multiplicacion(self,other):
        a=self.real
        b=self.compleja
        c=other.real
        d=other.compleja
        return((a*c-b*d,b*c+a*d))
    def division(self,other):
        a=self.real
        b=self.compleja
        c=other.real
        d=other.compleja
        comun=c**2+d**2
        return(((a*c+b*d)/comun,(b*c-a*d)/comun))
    def norma(self):
        a=self.real
        b=self.compleja
        return((a**2+b**2)**(1/2))
#referencia:
#http://maralboran.org/wikipedia/index.php/N%C3%BAmeros_complejos:_Operaciones_%281%C2%BABach%29

#Creación objetos
z=Compleja(2,1)#Notación:(parte real,parte imaginaria)
y=Compleja(3,4)
w=Compleja(3,1)
#ejemplo suma:
print(w.suma(z))
print(w.suma(y))
print('------------')
#ejemplo resta:
print(w.resta(z))
print(w.resta(y))
print('------------')
#ejemplo multiplicación:
print(w.multiplicacion(z))
print(w.multiplicacion(y))
print('------------')
#ejemplo división
print(w.division(z))
print(w.division(z))
print('----------')
#ejemplo norma
print(w.norma())
print(z.norma())




# In[ ]:




