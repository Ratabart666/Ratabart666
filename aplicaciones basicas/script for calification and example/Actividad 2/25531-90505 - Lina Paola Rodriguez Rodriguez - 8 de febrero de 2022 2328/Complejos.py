# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:57:59 2022

@author: ACER
"""

import numpy as np

class compleja:    
   def __init__(self, real, imaginario):#Se definen los atributos de la clase.
       self.real = real #El primer atributo comprende la parte real
       self.imaginario = imaginario #El segundo atributo comprende la parte compleja
     
   def suma(self,otro): #Se define la función suma para los objetos de la clase.
       normal = self.real + otro.real #Se suman las partes reales.
       imag = self.imaginario + otro.imaginario #Se suman las partes complejas
       cadena_imag = str(imag) #Pasar de int a str
       if cadena_imag [0] == "-": #Condicional que permite que el formato salga con el signo adecuado
          rta = str(normal) + "" + str(imag) + "i"
       else:   
          rta = str(normal) + " +"  + " " + str(imag) + "i" #Formato del resultado que debe arrojar la prueba
       return rta
       
   def resta(self,otro): #Se define la función resta para los objetos de la clase.
       normal = self.real - otro.real #Se restan las partes reales 
       imag = self.imaginario - otro.imaginario #Se restan las partes complejas
       cad_imag = str(imag) #Pasar imag de int a str
       if cad_imag [0] == "-": #Condicional que permite colocar el formato con el signo adecuado.
          rta = str(normal) + " " + str(imag) + "i"
       else:   
          rta = str(normal) + " + "  + str(imag) + "i" #Formato del resultado que debe arrojar la prueba
       return rta
       
   def multiplicacion(self,otro): #Se define la funcion multiplicacion para los objetos de la clase
       # (a+bi)*(c+di) = ac + adi + cbi + bidi = ac + bd*(-1) + (ad + cb)i
       a1 = self.real*otro.real #Se multiplica la parte real a*c
       a2 = self.real*otro.imaginario #Se multiplica la parte real del primero con la imaginaria del segundo
       a3 = self.imaginario*otro.real #Se multiplica la parte imaginaria del primero con la real del segundo
       a4 = (self.imaginario*otro.imaginario)*(-1) #Se multiplican las partes imaginarias
       a5 = a2 + a3 #Se suman las partes adi y cbi
       a6 = a1 + a4 #Se suma ab por bd(-1)
       final = str(a6) + "" + " + " + str(a5) + "i" #Formato del resultado que debe arrojar la prueba
       return final
       
   def division(self,otro): #Se define la funcion division para los objetos de la clase
       inverso1 = otro.real  #Se usa para sacar el inverso multiplicativo
       inverso2 = (-otro.imaginario) #Se usa para sacar el inverso multiplicativo.
       b1 = self.real*inverso1 #Operaciones iguales que en la multiplicacion
       b2 = self.real*inverso2 #Operaciones iguales que en la multiplicacion
       b3 = self.imaginario*inverso1 #Operaciones iguales que en la multiplicacion
       b4 = self.imaginario*inverso2*(-1) #Operaciones iguales que en la multiplicacion
       b5 = otro.real*inverso1 #Se usa para calcular el denominador 
       b6 = otro.imaginario*(-inverso2) #Se usa para calcular el denominador
       b7 = b1+b4 #Suma de terminos semejantes
       b8 = b3+b2 #Suma de terminos semejantes
       b9 = b5+b6 #Suma para resultado del denominador
       resp_real= b7/b9 #Division parte real con denominador obtenido
       resp_imaginaria = b8/b9 #Division parte parte imaginaria con denominador obtenido
       resp_final= str(resp_real) + " + " + str(resp_imaginaria) + "i" #Formato de la respuesta a mostrar
       return resp_final
       
   def norma(self,otro): #Muestra la norma de un numero complejo
       x1 = np.sqrt(((self.real*self.real)+(self.imaginario*self.imaginario))) #Formula para calcular norma
       x2 = np.sqrt(((otro.real*otro.real)+(otro.imaginario*otro.imaginario))) #Formula para calcular norma
       respuesta = "La norma #1 es " + str(x1) + " y la norma del #2 es " + str(x2)
       return respuesta #Arroja la norma del numero complejo
   
#Pruebas realizadas por cada una de las funciones.   
a=compleja(1,2)
b=compleja(3,-5)
c=compleja(3,2)
d=compleja(3,4)
e=compleja(2,3)
f=compleja(4,6)    
print (compleja.suma(a,b))
print (compleja.suma(c,d))
print (compleja.suma(e,f))
print (compleja.resta(a,b))
print (compleja.resta(c,d))
print (compleja.resta(e,f))
print (compleja.multiplicacion(a,b))
print (compleja.multiplicacion(c,d))
print (compleja.multiplicacion(e,f))
print (compleja.division(a,b))
print (compleja.division(c,d))
print (compleja.division(e,f))
print (compleja.norma(a,b))
print (compleja.norma(c,d))
print (compleja.norma(e,f))












