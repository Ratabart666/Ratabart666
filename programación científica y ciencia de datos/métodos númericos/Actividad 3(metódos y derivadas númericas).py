import numpy as np
import matplotlib.pyplot as plt




#funciones
def f(x,n):
    if n==1:
        y=np.cos(x)
    if n==2:
        y=(1/x**6)-(1/x**12)
    return y




#Derivadas (para cada metódo se hacen 2 ejemplos, estos mismos ejemplos tienen asociados un h pequeño y un h grande)




#paso grande
def derivada_progresiva(a,h,n):
    return(f(a+h,n)-f(a,n))/h

print('----------------------------------------------------------------------------')
print('La derivada progresiva en pi/6(h=0.1) de cos(x) es: ',derivada_progresiva(3.14/6,0.1,1))
print('La derivada progresiva en 10(h=0.1) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_progresiva(10,0.1,2))
print('----------------------------------------------------------------------------')



#paso pequeño
def derivada_progresiva(a,h,n):
    return(f(a+h,n)-f(a,n))/h


print('La derivada progresiva en pi/6(h=0.001) de cos(x) es: ',derivada_progresiva(3.14/6,0.001,1))
print('La derivada progresiva en 10(h=0.001) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_progresiva(10,0.001,2))
print('----------------------------------------------------------------------------')




#paso grande
def derivada_regresiva(a,h,n):
    return(f(a,n)-f(a-h,n))/h

print('La derivada regresiva en pi/6(h=0.1) de cos(x) es: ',derivada_regresiva(3.14/6,0.1,1))
print('La derivada regresiva en 10(h=0.1) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_regresiva(10,0.1,2))
print('----------------------------------------------------------------------------')




#paso pequeño
def derivada_regresiva(a,h,n):
    return(f(a,n)-f(a-h,n))/h

print('La derivada regresiva en pi/6(h=0.001) de cos(x) es: ',derivada_regresiva(3.14/6,0.001,1))
print('La derivada regresiva en 10(h=0.001) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_regresiva(10,0.001,2))
print('----------------------------------------------------------------------------')




#paso grande
def derivada_central(a,h,n):
    return(f(a+h,n)-f(a-h,n))/(2*h)

print('La derivada central en pi/6(h=0.1) de cos(x) es: ',derivada_central(3.14/6,0.1,1))
print('La derivada central en 10(h=0.1) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_central(10,0.1,2))
print('----------------------------------------------------------------------------')




#paso pequeño
def derivada_central(a,h,n):
    return(f(a+h,n)-f(a-h,n))/(2*h)

print('La derivada central en pi/6(h=0.001) de cos(x) es: ',derivada_central(3.14/6,0.001,1))
print('La derivada central en 10(h=0.001) de (1*10**-6/x**6)-(1*10**-6/x**12) es: ',derivada_central(10,0.001,2))
print('----------------------------------------------------------------------------')




#Gráfica derivada del coseno con h grande (azul:función, verde:derivada)




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_central(x,0.1,1),color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada central(h=0.1)')




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_progresiva(x,0.1,1),color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada progresiva(h=0.1)')




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_regresiva(x,0.1,1),color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada regresiva(h=0.1)')




#Gráfica derivada del coseno con h pequeña




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_central(x,0.001,1),0.1,color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada central(h=0.001)')




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_progresiva(x,0.001,1),0.1,color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada progresiva(h=0.001)')




fig,ax=plt.subplots()
x=np.linspace(-4,4,100)
ax.plot(x,derivada_regresiva(x,0.001,1),0.1,color='green')
ax.plot(x,f(x,1))
ax.set_title('gráfica derivada del coseno con derivada regresiva(h=0.001)')




#Gráfica derivada segunda función con h grande




fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_central(x,0.1,2),color='green')
ax.plot(x,f(x,2))
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada central(h=0.1)')




fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_progresiva(x,0.1,2),color='green')
ax.plot(x,f(x,2))
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada progresiva(h=0.1)')




fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_regresiva(x,0.1,2),color='green')
ax.plot(x,f(x,2))
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada regresiva(h=0.1)')




#Gráfica derivada segunda función con h pequeña




fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_central(x,0.001,2),color='green')
ax.plot(x,f(x,2))
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada central(h=0.001)')

#La linea vertical es una singularidad cuando x=0





fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_progresiva(x,0.001,2),color='green')
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada progresiva(h=0.001)')
ax.plot(x,f(x,2))


# In[167]:


fig,ax=plt.subplots()
x=np.linspace(-10,-1,100)
ax.set_xlim(-10,-1)
ax.set_ylim(-4,4)
ax.plot(x,derivada_regresiva(x,0.001,2),color='green')
ax.set_title('gráfica derivada de y=(1/x**6)-(1/x**12) con derivada regresiva(h=0.001)')
ax.plot(x,f(x,2))

#máximos y mínimos:
    

def validacion(x,n):
    x=True
    if x==0 and n==2:
        x=False
    if n!=1 and n!=2:
        x=False
    return x

def f(x,n):
    y='Ingrese un valor válido de n(n=1 y=cos(x),n=2 y=(1/x**6)-(1/x**12)'
    if n==1:
        y=np.cos(x)
    if n==2 and x!=0:
        y=(1/x**6)-(1/x**12)
    if n==2 and x==0:
        y='Debido al comportamiento de la  y=(1/x**6)-(1/x**12) ingrese un valor diferente de 0'
    return y


def derivada1(n,x):
    derivada1='Ingrese un valor válido de n(n=1 y=cos(x),n=2 y=(1/x**6)-(1/x**12)'
    if n==1:
        derivada1=-np.sin(x)
    if n==2 and x!=0:
        derivada1=(-6/x**7)+(12/x**13)
    if n==2 and x==0:
        derivada1='Debido al comportamiento de la  y=(1/x**6)-(1/x**12) ingrese un valor diferente de 0 o el metodo falló al encontrar un punto 0'
    return derivada1

def derivada2(n,x):
    derivada2='Ingrese un valor válido de n'
    if n==1:
        derivada2=-np.cos(x)
    if n==2 and x!=0:
        derivada2=(42/x**8)-(156/x**14)
    if n==2 and x==0:
        derivada2='Debido al comportamiento de la función ingrese un valor diferente de 0'
    return derivada2
    
    

def newton(x0,e,n): #primera coseno, segunda función y=(1/x**6)-(1/x**12)
#punto inicial de la interación,error,función(1 para coseno 2 para (1/x**6)-(1/x**12) )
    extremo=['minímo','máximo','punto inflexión']
    list=[]
    xant=x0
    if validacion(xant,n)==False:
        print('Error:')
        print('Usted ingreso x=0 en la función y=(1/x**6)-(1/x**12)')
        print('o ingreso un n no válido(n=1 y=cosx, n=2 y=(1/x**6)-(1/x**12)')
        return '¡Corriga!'
    else:   
        xsig=xant-(derivada1(n,xant)/derivada2(n,xant))
        xsig=xant-(derivada1(n,xant)/derivada2(n,xant))
        while abs(xsig-xant)>e:
            xant=xsig    
            xsig=xant-(derivada1(n,xant)/derivada2(n,xant))
        list.append(xsig)
        if derivada2(n,xsig)>0:
                list.append(extremo[0])
        if derivada2(n,xsig)<0:
                list.append(extremo[1])
        else:
            list.append(extremo[2])
        return 'En el punto ('+str(list[0])+','+str(f(list[0],n))+') se encuentra un: '+str(list[1])

print('Máximo y minimos de las funciones')
print(' ')
print('Precisión pequeña 0.1')
print(' ')
print('Máximos de la función y=(1/x**6)-(1/x**12)')
print(newton(-1,0.1,2))
print(newton(1,0.1,2))
print(' ')
print('Un minímo y un máximo para y=cosx')
print(newton(1,0.1,1))
print(newton(3,0.1,1))
print('----------------------------------------------------------------------------')
print('presición grande 0.001')
print(' ')
print('Máximos de la función y=(1/x**6)-(1/x**12)')
print(newton(-1,0.1,2))
print(newton(1,0.1,2))
print(' ')
print('Un minímo y un máximo para y=cosx')
print(newton(1,0.001,1))
print(newton(3,0.001,1))





    


        



