# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:17:08 2021

@author: Asus
"""

def diametro_escala(orden_magnitud:int,numero:float)->float:
    x=(2*numero)*(10**orden_magnitud)
    y=0.62*(10**-8)
    z=x*y
    return z
def distancia_sol_escala(orden_magnitud:int,numero:float)->float:
    x=(numero)*(10**orden_magnitud)
    y=0.62*(10**-8)
    z=x*y
    return z
