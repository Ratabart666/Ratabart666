
def bisiesto(anio:int)->bool:
    x=False
    if anio%4!=0:
        x=False
    elif anio%100!=0:
        x=True 
    elif anio%400!=0:
        x=False   
    else:
        x=True
    return x
def clasificar (a1:float,a2:float,a3:float)->str:
    if a1+a2+a3!=180:
        x=str('La suma de los ángulos no es 180 grados')
    elif a1+a2+a3==180:
        if a1==60 and a2==60 and a3==60:
            x=str('Equilatero')
        elif a1==a2 or a1==a3 or a2==a3:
            x=str('Isósceles')
        else:
            x=str('Escaleno')
    return x
def solucionar(a:float,b:float,c:float)->str:
    if b**2-4*a*c<0:
        x=str('No tiene solución')
    else:
        y1=(-b-(b**2-4*a*c)**(1/2))/(2*a)
        y2=(-b+(b**2-4*a*c)**(1/2))/(2*a)
        x=str(y1)+str(' ')+str(y2)
    return x


print(bisiesto(2003))