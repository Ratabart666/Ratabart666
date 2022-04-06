"""
Created on Sat Mar 12 14:22:13 2022

@author: Asus
"""
import warnings
warnings.filterwarnings("ignore")

def productoria(list):
    '''Ingresada una lista devuelve el producto de todos sus elementos
        Parametros:
            list:lista con los elementos
        Retorno
            Producto de todos sus elementos'''
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues*list[i]
    return despues

def sumatoria(list):
    '''Ingresada una lista devuelve la suma de todos sus elementos
        Parametros:
            list:lista con los elementos
        Retorno
            Suma de todos sus elementos'''
    despues=list[0]
    for i in range(1,len(list)):
        despues=despues+list[i]
    return despues

def interpolacionlagrange(x,X,Y):
    '''Ingresada un valor de x, una lista de valores de X y de Y devuelve la interpolacion de lagrange evaluada en x
        Parametros:
            x:valor de x
            X:valores de x
            Y:valores de y
        Retorno
            Interpolacion de lagrange evaluada en x'''
    
    coeficientes=Y
    polinomios_x=[]
    auxiliar=[]
    for i in range(0,len(X)):
        for j in range(0,len(X)): 
            if i!=j:
                auxiliar.append((x-X[j])/(X[i]-X[j]))
        polinomios_x.append(productoria(auxiliar)*coeficientes[i])
        auxiliar=[]
    return sumatoria(polinomios_x)


def derivada_numerica1(x_values,y_values,loc):
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localizacion de un
        punto en x, retorna la derivada numerica en ese punto.
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localizacion en la lista del valor de x que queremos evaluar
    Retorno:
        Derivada evaluada numericamente en el punto deseado
    '''
    y_values[0]
    if loc!=0 and loc!=len(x_values)-1:
        return (y_values[loc+1]-y_values[loc-1])/(2*(x_values[1]-x_values[0]))  
    elif loc==0:
        return (y_values[loc+1]-y_values[loc])/((x_values[1]-x_values[0]))  
    elif loc==len(x_values)-1:
        return (y_values[loc]-y_values[loc-1])/((x_values[1]-x_values[0]))  

def derivada_numerica2(x_values,loc,funcion):
    '''Ingresados los valores de x,y la localizacion de un punto en x,
        retorna la derivada numerica en ese punto con h=10**-6
        Defina la funcion como funcion(x)
    Parametros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion:funcion deseada
    Retorno:
        Derivada evaluada numericamente en el punto deseado
    '''
    h=10e-6
    return (funcion(x_values[loc]+h)-funcion(x_values[loc]-h))/(2*h)

def segunda_derivada_numerica1(x_values,y_values,loc):
    '''Ingresados los valores de x(equisdistantes),los valores de y,y la localizacion de un
        punto en x, retorna la segunda derivada numerica en ese punto
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
        loc: localizacion en la lista del valor de x que queremos evaluar
    Retorno:
        Segunda Derivada evaluada nÃºmericamente en el punto deseado. Atencion La funcion evalua en puntos diferentes del inicial y final.
    '''
    return((y_values[loc+1]-2*y_values[loc]+y_values[loc-1])/((x_values[1]-x_values[0])**2))

def segunda_derivada_numerica2(x_values,loc,funcion):
    '''Ingresados los valores de x,y la localizacion en el
        punto en x, retorna la segunda derivada numerica en ese punto con h=10**-6
        Defina la funcion como funcion(x)
    Parametros: 
        x_values: Valores de x
        loc: localizacion en la lista del valor de x que queremos evaluar
        funcion: funcion deseada
    Retorno:
        Segunda Derivada evaluada nÃºmericamente en el punto deseado
    '''
    h=10e-6
    funcion(x_values[loc]-h)
    return((funcion(x_values[loc]+h)-2*funcion(x_values[loc])+funcion(x_values[loc]-h))/((h)**2))

def lista_derivada_numerica1(x_values,y_values):
    '''Ingresados los valores de x y los valores de y, se retorna las derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
    Retorno:
        lista con las derivadas numericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica1(x_values, y_values,i))
    return list

def lista_derivada_numerica2(x_values,funcion):
    '''Ingresados los valores de x y la funcion deseada, se retorna las derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        funcion: funcion deseada
    Retorno:
        lista con las derivadas numericas
    '''

    list=[]
    for i in range(0,len(x_values)):
        list.append(derivada_numerica2(x_values,i,funcion))
    return list

def lista_segunda_derivada_numerica1(x_values,y_values):
    '''Ingresados los valores de x y los valores de y, se retorna las segundas derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        y_values: Valores de y
    Retorno:
        lista con las segundas derivadas numericas
    '''
    list=[]
    for i in range(1,len(x_values)-1):
        list.append(segunda_derivada_numerica1(x_values,y_values,i))
    return list

def lista_segunda_derivada_numerica2(x_values,funcion):
    '''Ingresados los valores de x y la función, retorna lista de las segundas derivadas numericas
    Parametros: 
        x_values: Valores equisdistantes de x(valores crecientes)
        funcion: funcion deseada
    Retorno:
        lista con las segundas derivadas numericas
    '''
    list=[]
    for i in range(0,len(x_values)):
        list.append(segunda_derivada_numerica2(x_values,i,funcion))
    return list

def newton_raphson_derivada_conocida(x0,funcion,derivada): 
    '''Ingresados los valores de x0, la funcion y la derivada
        retorna la solucion numerica, porfavor verifique que la funcion no cambie de
        concavidad y la derivada sea diferente de 0 en el intervalo de convergencia, y asegure un intervalo de convergencia; 
        de lo contrario el programa puede no funcionar(Puede asegurar el intervalo gráficamente).
        Defina la funcion como f(x).
    Parametros: 
        x0: valor inicial
        función: función
        derivada: derivada
    Retorno:
        Solucion numerica newton-raphson
        
    '''
    xantes=x0
    xdespues=xantes-(funcion(xantes)/derivada(xantes))
    while (xdespues-xantes)/xantes>10e-6:
        xantes=xdespues
        xdespues=xantes-(funcion(xantes)/derivada(xantes))
    return xdespues

def newton_raphson_derivada_desconocida(x0,funcion): 
    '''Ingresados los valores de x y y
        retorna la solucion numerica(En caso que la derivada sea complicada), porfavor verifique que la funcion no cambie de
        concavidad y la derivada sea diferente de 0 en el intervalo de convergencia, y asegure un intervalo de convergencia; de lo contrario el programa puede no funcionar(Puede asegurar el intervalo gráficamente).
        Defina la funcion como f(x).
    Parametros: 
        x0: valor inicial
        funcion: función conocida.
    Retorno:
        Solucion numerica newton-raphson
    '''
    xantes=x0
    xdespues=x0-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    while  (xdespues-xantes)/xantes<10e-6:
        xantes=xdespues
        xdespues=xantes-(funcion(xantes)/derivada_numerica2([xantes],0,funcion))
    return xdespues

def integral_riemann(f,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(riemann) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(riemann)'''
    Δx=(b-a)/1000
    I=0
    for i in range(0,1000):
        xi=a+i*Δx
        I+=f(xi)*Δx
    return I

def integral_trapecio(f,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(trapecio) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(trapecio)'''
    Δx=(b-a)/1000
    yi=f(a)
    yf=f(b)
    sigmaf=0
    xi=0
    for i in range(1,1000):
        xi=a+i*Δx
        sigmaf+=f(xi)
        
    I=Δx*((yi/2)+sigmaf+(yf/2))
    return I

from scipy.special import roots_legendre

def intregral_gauss_legendre(funcion,a,b):
    '''Ingresada la funcion, los limites de integracion(1000 particiones) devuelve la integral numerica(gauss legendre) aproximada
        Parametros:
            f:funcion
            a: intervalo inferior
            b: intervalo superior
            n: numero de intervalos
       Retorno
           Devuelve la integral numerica(gauss legendre)'''
    
    x,integral=0,0
    raices,pesos=roots_legendre(1000)
    for i in range(0,1000):
        x=(1/2)*(raices[i]*(b-a)+a+b)
        integral+=funcion(x)*pesos[i]
    integral=(1/2)*(b-a)*integral        
    return integral

def integral_riemann_funciondes(X,Y,loc1,loc2):
    '''Ingresada una serie de datos, los limites de integracion(1000 particiones) devuelve la integral numerica(riemann) aproximada(No elija como intervalo superior el ultimo datos en X)
        Parametros:
            X:valores de x 
            Y: valores de y
            loc1: intervalo inferior
            loc2: intervalo superior
       Retorno
           Devuelve la integral numerica(riemann)'''
    Δx=None
    I=0
    for i in range(loc1,loc2):
        Δx=X[i+1]-X[i]
        I+=Y[i]*Δx
    return I

def integral_trapecio_funciondes(X,Y,loc1,loc2):
    '''Ingresada una serie de datos, los limites de integracion(1000 particiones) devuelve la integral numerica(trapecio) aproximada(No elija como intervalo superior el ultimo datos en X)
        Parametros:
            X:valores de x 
            Y: valores de y
            loc1: intervalo inferior
            loc2: intervalo superior
       Retorno
           Devuelve la integral numerica(trapecio)'''
    Δx=None
    I=0
    aux=0
    for i in range(loc1,loc2):
        Δx=X[i+1]-X[i]
        aux=(Y[i]+Y[i+1])/2
        I+=aux*Δx
    return I

def matriz_vacia(n,m):
    '''Ingresados los valores deseados de columnas y filas
        retorna una matriz vacía de nxm
    Parametros: 
        n: numero de filas
        m: numero de columnas
    Retorno:
        Matriz vacia de nxm
    '''
    vacia=[]
    for i in range(0,n):
         vacia.append([])
    for j in vacia:
         for k in range(0,m):
             j.append(0)
    return vacia

def print_matriz(matriz):
    '''Imprime la matriz de manera organizada
    '''
    aux=matriz_vacia(len(matriz),len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            aux[i][j]=round(matriz[i][j],6)
            
    for i in range(0,len(matriz)):
            print(aux[i])
    return(' ')  
          
def columnaj(matriz,j):
    '''Ingresados la columna deseada
        retorna esta columna
    Parametros: 
        matriz: matriz deseada
        m: columna deseada(la primera columna es 1)
    Retorno:
        columna deseada
    '''
    j=j-1
    columna=[]
    for i in range(0,len(matriz)):
        columna.append(matriz[i][j])
    return columna

def producto_punto(vector1,vector2):
    '''Ingresados 2 vectores
        retorna su producto punto
    Parametros: 
        vector1: vector 2
        vector2: vector 1
    Retorno:
        producto punto
    '''
    productopunto=0
    for k in range(0,len(vector1)):
          productopunto+=vector1[k]*vector2[k]
    return productopunto

def suma(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su suma
    Parametros: 
        matriz1: Matriz 2
        matriz2: Matriz 1
    Retorno:
        Retorna su suma
    '''
    suma=matriz_vacia(len(matriz1),len(matriz1[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz1[0])):
            suma[i][j]=matriz1[i][j]+matriz2[i][j]
    return suma

def resta(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su resta
    Parametros: 
        matriz1: Matriz 1
        matriz2: Matriz 2
    Retorno:
        Retorna Matriz 1 - Matriz 2
    '''
    resta=matriz_vacia(len(matriz1),len(matriz1[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz1[0])):
            resta[i][j]=matriz1[i][j]-matriz2[i][j]
    return resta

def producto(matriz1,matriz2):
    '''Ingresados 2 Matrices
        retorna su producto
    Parametros: 
        matriz1: Matriz 1
        matriz2: Matriz 2
    Retorno:
        Retorna Matriz 1*Matriz 2
    '''
    
    producto=matriz_vacia(len(matriz1),len(matriz2[0]))
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz2[0])):
            producto[i][j]=producto_punto(matriz1[i],columnaj(matriz2,j+1))
    return producto
    
def productoescalarmatriz(matriz,c):
    '''Ingresados 1 Matriz y un escalar
        retorna el producto
    Parametros: 
        matriz1: Matriz 
        c: Escalar
    Retorno:
        Retorna c*Matriz 1
    '''
    new=matriz_vacia(len(matriz),len(matriz[0]))
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
                new[i][j]=(matriz[i][j])*c
    return new

def eliminarfilai(matriz,i):
    '''Ingresados 1 Matriz y una fila 
        retorna la matriz sin la fila
    Parametros: 
        matriz1: Matriz 1
        i: Fila deseada(la primera fila es 1)
    Retorno:
        Matriz sin la fila i
    '''
    i=i-1
    new=[]
    for k in range(0,len(matriz)):
        if k!=i:
             new.append(matriz[k])
    return new

def eliminarcolumnaj(matriz,j):
    '''Ingresados 1 Matriz y una columna
        retorna la matriz sin la columna
    Parametros: 
        matriz1: Matriz 1
        j: Columna deseada(la primera columna es 1)
    Retorno:
        Matriz sin la Columna j
    '''
    j=j-1
    new=[]
    aux=[]
    for i in range(0,len(matriz)):
        for k in range(0,len(matriz[0])):
            if k!=j:
                aux.append(matriz[i][k])
        new.append(aux)
        aux=[]
    return new

def eliminar_filai_columnaj(matriz,i,j):
    '''Ingresados 1 Matriz,una fila y una columna
        retorna la matriz sin la fila y la columna
    Parametros: 
        matriz1: Matriz 1
        i: Fila deseada (la primera fila es 1)
        j: Columna deseada (la primera columna es 1)
    Retorno:
        Matriz sin la fila i y la columna j
    '''
    new=eliminarfilai(matriz,i)
    new=eliminarcolumnaj(new,j)
    return new

def transpuesta(A):
    '''Ingresada una matriz,devuelve su transpuesta
        Parametros:
            A: Matriz
        Retorno
            Matriz transpuesta'''
    B=matriz_vacia(len(A[0]),len(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i]=A[i][j]   
    return B

def multiplicar_vector_por_escalar(vector,c):
    '''Dada un vector y un escalar c, los multiplica
      Parametros:
            vector: vector
            c: escalar
        Retorno:
            vector por escalar'''
    
    new=[]
    for i in vector:
        new.append(c*i)
    return new
   
def restar_vectores(vector1,vector2):
    '''Dado 2 vectores,devuelve su resta
      Parametros:
            vector1: vector
            vector2: escalar
        Retorno:
            vector 1-vector 2'''
    new=[]
    for i in range(len(vector1)):
        new.append(vector1[i]-vector2[i])
    return new

def sumar_vectores(vector1,vector2):
    '''Dado 2 vectores,devuelve su suma
      Parametros:
            vector1: vector
            vector2: escalar
        Retorno:
            vector 1+vector 2'''
    new=[]
    for i in range(len(vector1)):
        new.append(vector1[i]+vector2[i])
    return new

def magnitud_vector(vector):
    '''Dado un vector retorna su norma
        Parametros:
            vector: vector
        Retorno
            Norma del vector'''
    norma=0
    for i in vector:
        norma+=i**2
    return (norma)**(1/2)

import numpy as np
def angulo_vectores(vector1,vector2):
    '''Dado 2 vectores, devuelve el angulo entre ellos
        Parametros:
            vector1: vector
            vector 2: vector
        Retorno:
            Angulo entre ellos(grados)'''
    costetha=(producto_punto(vector1,vector2))/(magnitud_vector(vector1)*magnitud_vector(vector2))
    tetha=np.arccos(costetha)
    return np.degrees(tetha)

def triangular_superior(A):
    '''Dada una matriz A(cuadrada), la transforma mediante o.e.f a una matriz triangular superior, no debe haber 0's en la diagonal
        Parametros:
            A:matriz
        Retorno:
            Matriz en forma triangular superior'''
    B=A
    rows=len(A)
    aux=None
    for i in range(rows):
        for j in range(i+1,rows):
            aux=multiplicar_vector_por_escalar(B[i],( B[j][i]/B[i][i] ) )
            B[j]=restar_vectores(B[j],aux)
    return B

def triangular_inferior(A):
    '''Dada una matriz A(cuadrada), la transforma mediante o.e.f a una matriz triangular inferior
        Parametros:
            A:matriz
        Retorno:
            Matriz en forma triangular inferior'''
    B=A
    rows=len(A)
    aux=None
    for i in range(rows-1,-1,-1):
        for j in range(i-1,-1,-1):
            aux=multiplicar_vector_por_escalar(B[i],( B[j][i]/B[i][i] ) )
            B[j]=restar_vectores(B[j],aux)
    return B

def red_gauss(A):
    '''Dada una matriz A que representa un sistema de ecuaciones lineales,aplica el algoritmo de reduccion de gauss
        primero la convierte en una matriz triangular superior y despues en una matriz diagonal donde las soluciones son explicitas
        (La matriz debe tener tamano nx(n+1)) y las diagonales deben ser diferentes de 0
        Parametros:
            A:matriz
        Retorno:
            Solucion sistemas de ecuaciones lineales'''
    B=triangular_superior(A)
    B=triangular_inferior(B)
    for i in range(len(B)):
        B[i]=multiplicar_vector_por_escalar(B[i],1/(B[i][i]))
    return B

def indmaxarg(vector):
    '''Dado un vector retorna el indice con mayor valor
        Parametros:
            vector: vector
        Retorno
            Indice con mayor valor(el primer indice es 0)'''
    aux=max(vector)
    for i in range(len(vector)):
        if vector[i]==aux:
             return i
         
def absvector(vector):
    '''Dado un vector retorna sus coordenadas con valor absoluto
        Parametros:
            vector: vector
        Retorno
            coordenadas con valor absoluto'''
    for i in range(len(vector)):
        if vector[i]<0:
            vector[i]=-vector[i]
    return vector

def triangular_superior_con_pivoteo(A):
  '''Dada una matriz A(cuadrada), la transforma mediante o.e.f a una matriz triangular superior.
        Parametros:
            A:matriz
        Retorno:
            Matriz en forma triangular superior'''
  B=A
  rows=len(B)
  aux=None
  aux2=None
  d=0
  for i in range(rows):
    aux=columnaj(B,i)[i:len(columnaj(B,i))]
    aux=absvector(aux)
    indi_max=indmaxarg(aux)
    if indi_max>0:
      C=B[i]
      B[i]=B[i + indi_max]
      B[i + indi_max]=C
      d+=1
    for j in range(i+1,rows):
        aux2=multiplicar_vector_por_escalar(B[i],( B[j][i]/B[i][i] ) )
        B[j]=restar_vectores(B[j],aux2)
  return B,d

def red_gauss_gen(A):
    '''Dada una matriz A que representa un sistema de ecuaciones lineales,aplica el algoritmo de reduccion de gauss
        primero la convierte en una matriz triangular superior y despues en una matriz diagonal donde las soluciones son explicitas
        (La matriz debe tener tamano nx(n+1))
        Parametros:
            A:matriz
        Retorno:
            Solucion sistemas de ecuaciones lineales'''
    B=triangular_superior_con_pivoteo(A)[0]
    B=triangular_inferior(B)
    for i in range(len(B)):
        B[i]=multiplicar_vector_por_escalar(B[i],1/(B[i][i]))
    return B

def matriz_aum_id(A):
    '''Dada una matriz cuadrada a, retorna una matriz aumentada con la identidad
    Parametros:
        A:matriz
    Retorno
        Matriz aumentada con la identidad'''
    new=matriz_vacia(len(A),2*len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            new[i][j]=A[i][j]
    for i in range(len(A)):
        for j in range(len(A),2*len(A)):
            if i+len(A)==j:
                new[i][j]=1
            else:
                new[i][j]=0
    return new
    
def inversa(A):
  '''Dada una matriz cuadrada A, retorna su inversa
      Parametros:
          A: matriz
      Retorno:
          matriz inversa'''
  try:
      rows=len(A)
      B=matriz_aum_id(A)
      B=red_gauss_gen(B)
      for i in range(1,rows+1):
          B=eliminarcolumnaj(B,1)
      return B
  except:
      return('Matriz no cuadrada o input invalido')


def determinante(matriz):
   '''Dada una matriz cuadrada A,retorna su determinante
        Parametros:
            A: matriz
        Retorno
            determinante de A'''
   try:
       B,d=triangular_superior_con_pivoteo(matriz)
       signo=(-1)**d
       prod=1
       for i in range(len(B)):
           prod*=B[i][i]
       return signo*prod
   except:
       return 0

def remplazarcolumnaj(matriz,j,vector):
    '''Dada una matriz, su columna y un vector, remplaza la columna por el vector dado
        Parametros:
            matriz: matriz
            j: columna(primera columna 1)
            vector: vector que se desea remplazar
        Retorno:
            matriz con el elemento remplazado'''
    j=j-1
    for i in range(len(matriz)):
        matriz[i][j]=vector[i]
    return matriz

def vector_vacio(n):
    '''Dado un numero n, devuelve con un vector de dimension n con todas las entradas iguales a 0
        Parametros:
            n: numero de entradas
        Retorno:
           Vector: con n entradas y entradas iguales a 0'''
    aux=[]
    for i in range(n):
        aux.append(0)
    return aux

def calcula_qj(Q,aj,j,n):
  '''Funcion auxiliar que calcula el vector ortonormal qj, no es de utilidad solo es una funcion auxiliar de gram_schmidt'''
  suma=vector_vacio(n)
  aux=None
  for i in range(j):
    aux=multiplicar_vector_por_escalar(columnaj(Q,i),producto_punto(aj,columnaj(Q,i)))
    suma=sumar_vectores(suma,aux)
  aj_p=restar_vectores(aj,suma)
  return multiplicar_vector_por_escalar(aj_p,1/magnitud_vector(aj_p))

def gram_schmidt(A):
  '''Dada una matriz cuadrada, cuyas columnas son bases para R**n, devuelve una matriz ortogonal a traves del proceso de ortonormalizacion de gram-schmidt
      Parametros:
          A: matriz
      Retorno:
          matriz ortogonal'''
  columns=len(A[0])
  Q=matriz_vacia(len(A),len(A[0]))  
  Q=remplazarcolumnaj(Q,1,multiplicar_vector_por_escalar(columnaj(A,1),1/magnitud_vector(columnaj(A,1))))#columnaj(Q,1)/magnitud_vector(columnaj(Q,1)))
  for j in range(1,columns+1):
    Q=remplazarcolumnaj(Q,j,calcula_qj(Q,columnaj(A,j),j,columns))
  return Q

def factorizacionQR(A):
    Q=gram_schmidt(A)
    R=producto(transpuesta(Q),A)
    print('Q=')
    print(print_matriz(Q))
    print('R=')
    print(print_matriz(R))
    return ''

def diagonal(A):
    '''Dada una matriz, retorna los valores de la diagonal
        Parametros:
            A: matriz
        Retorno:
            Valores de la diagonal'''
    columns=len(A[0])
    aux=[]
    for i in range(columns):
        aux.append(A[i][i])
    return aux

def print_vector(vector):
    '''Dado un vector, lo imprime de manera organizada'''
    aux=[]
    for i in vector:
        aux.append(round(i,6))
    return print(aux)

def valores_propios_algoritmo_QR(A):
  '''Dada una matriz cuadrada,se itera 100 veces, el algoritmo devuelve los valores propios a traves del algoritmo qr
      Parametros:
          A:matriz
          iteraciones: iteraciones del algoritmo
      Retorno:
          valores propios(reales) aproximados'''
  Ak=A
  for k in range(100):
    Qk=gram_schmidt(Ak)
    Ak=producto(producto(transpuesta(Qk),Ak),Qk)#Qk.T @ Ak @ Qk
  return print_vector(diagonal(Ak))

def transpuesta_vector(vector,aux):
    '''Dado un vector, retorna su transpuesta
    Parametros:
        vector:vector
        aux: 1(si es un vector columna) 2(si es un vector fila)
    Retorno
        vector transpuesta'''
    new=[]
    if aux==1:
        for i in vector:
            new.append(i[0])
    elif aux==2:
        for i in vector:
            new.append([i])
    return new

def vector_por_matriz(vector,matriz):
   '''Dado un vector y una matriz devuelve su producto'''
   vector=np.array(vector)
   matriz=np.array(matriz)
   return (vector @ matriz).tolist()
        
def matriz_por_vector(vector,matriz):
   '''Dada una matriz y un vector devuelve su producto'''
   vector=np.array(vector)
   matriz=np.array(matriz) 
   return (matriz @ vector).tolist()

def metodo_de_potencias(A):
  '''Dada una matriz cuadrada,se calcula el autovector de mayor autovalor
      Parametros:
          A:matriz
      Retorno:
          autovector con mayor autovalor'''
  A=np.array(A)
  new=[]
  iteraciones=1000
  for i in range(len(A)):
      new.append(1)
  v0=np.array(new)
  Av0=A @ v0
  v=Av0/(np.sqrt(sum(Av0 * Av0)))
  for i in range(iteraciones):
      v0=v
      Av0=A @ v0
      v=Av0/(np.sqrt(sum(Av0 * Av0)))
  return v.tolist()
             
def apro_mayor_valor_propio(A,v_prop):
  '''Dado una aproximacion al autovalor de mayor valor propio o un valor exacto, la funcion
    retorna una aproximacion al autovalor correspondiente
    Parametros:
        A:matriz
        v_prop: vector propio(fila)
    Retorno:
        Autovalor dominante'''
  A=np.array(A)
  v_prop=np.array(v_prop)
  return (v_prop.T @ A @ v_prop) / (v_prop @ v_prop)

import statistics as st 

#http://www1.monografias.com/docs115/regresion-lineal-multiple/regresion-lineal-multiple2.shtml
def regresion(x,y,grado,tupla):
    '''Ingresados valores de x,y y el grado del polinomio para la regresión,retorna los parámetros de la regresión
    Parametros
        x: valores de x
        y: valores de y
        grado: grado del polinomio a ajustar
       tupla: tupla que indica que coeficientes queremos diferentes de cero, ajuste(x**2+1)-> tupla=(1,0,1)(ascendente)
    Retorno
        Retorna los coeficientes de mayor a menor, la incertidumbre y el coeficiente de correlacion
        '''
    columnas=0
    aux=[]
    for i in range(len(tupla)):
        if tupla[i]==1:
            columnas+=1   
            aux.append(i)
    rows=len(x)
    A=matriz_vacia(rows,columnas)
    for i in range(len(aux)):
        A=remplazarcolumnaj(A,i+1,(np.array(x)**(aux[i])).tolist())
    v=matriz_por_vector(y,producto(inversa(producto(transpuesta(A),A)),transpuesta(A)))
    aux1=restar_vectores(matriz_por_vector(v,A),y)
    aux1=(magnitud_vector(aux1))**2
    if len(A)-len(A[0])-1!=0:
        aux2=len(A)-len(A[0])-1
    elif len(A)-len(A[0])-1==0:
        aux2=len(A)-len(A[0])
    sigma_2=(aux1/aux2)
    cov=inversa(producto(transpuesta(A),A))
    cov=productoescalarmatriz(cov,sigma_2)
    incer=[]
    media=st.mean(y)
    VT=sumatoria(((np.array(y)-media)**2).tolist())
    R_2=1-(sigma_2*(len(A)-1)/VT)
    R=(R_2)**(1/2)
    for i in range(len(cov)):
        incer.append((abs(cov[i][i]))**(1/2))
    return v[::-1],incer[::-1],R

import matplotlib.pyplot as plt

def aux_regresion(x,y,grado,tupla):
    '''Ingresados valores de x,y y el grado del polinomio para la regresión,retorna los datos de y ajustados a x
    Parametros
        x: valores de x
        y: valores de y
        grado: grado del polinomio a ajustar
       tupla: tupla que indica que coeficientes queremos diferentes de cero, ajuste(x**2+1)-> tupla=(1,0,1)(ascendente)
    Retorno
        Retorna los datos de y ajustados a x
        '''
    ajuste=regresion(x,y,grado,tupla)
    parametros=ajuste[0][::-1]
    x.sort()
    x=np.array((np.linspace(x[0],x[-1]),1000))[0]
    grados=[]
    yajus1=[]
    aux=None
    result=None
    for i in range(len(tupla)):
        if tupla[i]==1:
            grados.append(i)
    for i in range(len(parametros)):
       yajus1.append((parametros[i]*(x**(grados[i]))))
    result=yajus1[0]
    for i in range(1,len(yajus1)):
        aux=yajus1[i]
        result=aux+result
    return result
def dibujo_reg(x,y,grado,tupla,fila,columna,nombre,nombrex,nombrey,label,ax):
    '''Ingresados valores de x,y y el grado del polinomio para la regresión,retorna los datos ploteados en 2 dimensiones
    se compara experimento con ajuste, ( se debe antes crear el plano)
    si no cola subplot fila=columna=0, importe matplotlib
    --------------------------
    Colocar antes fig,ax = plt.subplots(filas(desde 0),columnas(desde 0),figsize=(eje x,ejey))
    ---------------------------
    Parametros
        x: valores de x
        y: valores de y
        grado: grado del polinomio a ajustar
       tupla: tupla que indica que coeficientes queremos diferentes de cero, ajuste(x**2+1)-> tupla=(1,0,1)(ascendente)
       fila: columna en el subplot empieza desde 0
       columna: columna en el subplot empieza desde 0
       nombre: Nombre gráfica
       nombrex: Nombre en x
       nombrey: Nombre en y
       label: Nombre de la linea

    Retorno
        Retorna los datos ploteados en una (figura ya hecha) en 2 dimensiones se compara experimento con ajuste'''
    plt.style.use('dark_background')
    x.sort()

    if columna==0 and fila==0:
        
        ax.scatter(x,y,label='datos'+label)
        x.sort()
        ax.plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresion(x,y,grado,tupla),label='ajuste'+label)
        ax.set_xlabel(nombrex)
        ax.set_ylabel(nombrey)
        ax.set_title(nombre)
        ax.legend()
    elif columna==0:
        
        ax[fila].scatter(x,y,label='datos'+label)
        x.sort()
        ax[fila].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresion(x,y,grado,tupla),label='ajuste'+label)
        ax[fila].set_xlabel(nombrex)
        ax[fila].set_ylabel(nombrey)
        ax[fila].set_title(nombre)
        ax[fila].legend()
        
    elif fila==0:
        ax[columna].scatter(x,y,label='datos'+label)
        x.sort()
        ax[columna].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresion(x,y,grado,tupla),label='ajuste'+label)
        ax[columna].set_xlabel(nombrex)
        ax[columna].set_ylabel(nombrey)
        ax[columna].set_title(nombre)
        ax[columna].legend()
        
    else:
        
        ax[fila][columna].scatter(x,y,label='datos'+label)
        x.sort()
        ax[fila][columna].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresion(x,y,grado,tupla),label='ajuste'+label)
        ax[fila][columna].set_xlabel(nombrex)
        ax[fila][columna].set_ylabel(nombrey)
        ax[fila][columna].set_title(nombre)
        ax[fila][columna].legend()

def regresionlineal(x,y):
    mediay=st.mean(y)
    mediax=st.mean(x)
    sigma1=0
    sigma2=0
    sigma4=0
    sigma5=0
    sigma6=0
    sigma7=0
    sigma8=0
    for i in range(len(x)):
        sigma1+=x[i]*(y[i]-mediay)
        sigma2+=x[i]*(x[i]-mediax)
    m=sigma1/sigma2
    b=mediay-m*mediax
    coeficientes=[m,b]
    for i in range(len(x)):
        sigma4+=(y[i]-b-m*x[i])**2
    varianza=(sigma4/(len(x)-2))**(1/2)
    error_m=varianza*((len(x)/sigma2)**(1/2))
    for i in range(len(x)):
        sigma5+=x[i]**2
    error_b=varianza*((sigma5/sigma2)**(1/2))
    errores=[error_m,error_b]
    for i in range(len(x)):
        sigma6+=abs((x[i]-mediax)*(y[i]-mediay))
        sigma7+=(x[i]-mediax)**2
        sigma8+=(y[i]-mediay)**2
    r=sigma6/((sigma7*sigma6)**(1/2))
    return coeficientes,errores,r
#https://glosarios.servidor-alicante.com/terminos-estadistica/coeficiente-de-correlacion-lineal-de-pearson

def aux_regresionlin(x,y):
    '''Ingresados valores de x,y y el grado del polinomio para la regresión,retorna los datos de y ajustados a x
    Parametros
        x: valores de x
        y: valores de y
        grado: grado del polinomio a ajustar
       tupla: tupla que indica que coeficientes queremos diferentes de cero, ajuste(x**2+1)-> tupla=(1,0,1)(ascendente)
    Retorno
        Retorna los datos de y ajustados a x
        '''
    ajuste=regresionlineal(x,y)
    parametros=ajuste[0][::-1]
    x.sort()
    x=np.array((np.linspace(x[0],x[-1]),1000))[0]
    grados=(0,1)
    yajus1=[]
    aux=None
    result=None
    for i in range(len(parametros)):
       yajus1.append((parametros[i]*(x**(grados[i]))))
    result=yajus1[0]
    for i in range(1,len(yajus1)):
        aux=yajus1[i]
        result=aux+result
    return result
def dibujo_reglineal(x,y,fila,columna,nombre,nombrex,nombrey,ax,label):
    '''Ingresados valores de x,y y el grado del polinomio para la regresión,retorna los datos ploteados en 2 dimensiones
    se compara experimento con ajuste, ( se debe antes crear el plano)
    si no cola subplot fila=columna=0, importe matplotlib
    --------------------------
    Colocar antes fig,ax = plt.subplots(filas(desde 0),columnas(desde 0),figsize=(eje x,ejey))
    ---------------------------
    Parametros
        x: valores de x
        y: valores de y
        grado: grado del polinomio a ajustar
       tupla: tupla que indica que coeficientes queremos diferentes de cero, ajuste(x**2+1)-> tupla=(1,0,1)(ascendente)
       fila: columna en el subplot empieza desde 0
       columna: columna en el subplot empieza desde 0
       nombre: Nombre gráfica
       nombrex: Nombre en x
       nombrey: Nombre en y
       label: Nombre de la linea

    Retorno
        Retorna los datos ploteados en una (figura ya hecha) en 2 dimensiones se compara experimento con ajuste'''
    plt.style.use('dark_background')
    x.sort()

    if columna==0 and fila==0:
        
        ax.scatter(x,y,label='datos'+label)
        x.sort()
        ax.plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresionlin(x,y),label='ajuste'+label)
        ax.set_xlabel(nombrex)
        ax.set_ylabel(nombrey)
        ax.set_title(nombre)
        ax.legend()
    elif columna==0:
        ax[fila].scatter(x,y,label='datos'+label)
        x.sort()
        ax[fila].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresionlin(x,y),label='ajuste'+label)
        ax[fila].set_xlabel(nombrex)
        ax[fila].set_ylabel(nombrey)
        ax[fila].set_title(nombre)
        ax[fila].legend()
    elif fila==0:
        ax[columna].scatter(x,y,label='datos'+label)
        x.sort()
        ax[columna].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresionlin(x,y),label='ajuste'+label)
        ax[columna].set_xlabel(nombrex)
        ax[columna].set_ylabel(nombrey)
        ax[columna].set_title(nombre)
        ax[columna].legend()
    else:
        
        ax[fila][columna].scatter(x,y,label='datos'+label)
        x.sort()
        ax[fila][columna].plot(np.array((np.linspace(x[0],x[-1]),1000))[0],aux_regresionlin(x,y),label='ajuste'+label)
        ax[fila][columna].set_xlabel(nombrex)
        ax[fila][columna].set_ylabel(nombrey)
        ax[fila][columna].set_title(nombre)
        ax[fila][columna].legend()
        
        
