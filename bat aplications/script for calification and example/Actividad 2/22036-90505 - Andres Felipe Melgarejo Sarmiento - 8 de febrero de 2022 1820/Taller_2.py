# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:13:56 2022

@author: FELIP
"""

class complejos:
    def __init__(self,real,imag):
        self.real= real
        self.imag=imag
        
    #Operaciones
    def suma(self,other):
        a=self.real+other.real
        b=self.imag+other.imag
        return a,b
        
    def resta(self,other):
        c=self.real-other.real
        d=self.imag-other.imag
        return c,d
    
    def producto(self,other):
        d=((self.real*other.real)-(self.imag*other.imag))
        e=((self.imag*other.real)+(self.real*other.imag))
        return d,e
    
    def cociente(self,other):
        re=self.real
        re_=other.real
        im=self.imag
        im_=other.imag
        
        f= ((re*re_)+(im*im_))/(re_**2 + im_**2)
        g= ((im*re_)-(re*im_))/(re_**2 + im_**2)
        
        return f,g
    
    def norma(self,other):
        re=self.real
        im=self.imag
        
        
        h=(((re**2)+(im**2))**1/2)
        return h
