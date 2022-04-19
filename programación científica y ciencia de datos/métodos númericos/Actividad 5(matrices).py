# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:00:28 2022

@author: Asus
"""

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
    print(' ')
    return ' '
          
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
    
def productoescalar(matriz,c):
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
                new[i][j]=matriz[i][j]*c
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
  rows=len(A)
  B=matriz_aum_id(A)
  B=red_gauss_gen(B)
  for i in range(1,rows+1):
      B=eliminarcolumnaj(B,1)
  return B

def determinante(matriz):
   '''Dada una matriz cuadrada A,retorna su determinante
        Parametros:
            A: matriz
        Retorno
            determinante de A'''
   B,d=triangular_superior_con_pivoteo(matriz)
   signo=(-1)**d
   prod=1
   for i in range(len(B)):
        prod*=B[i][i]
   return signo*prod

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
    print(aux)
    return print(' ')

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


print('Estos son los ejemplos(se utilizan las matrices a continuación el orden es A,B,C,D,b(vector)):')
A=[[1,2,3],[4,5,6]]
B=[[6,5,4],[3,2,1]]
C=[[1,2],[3,4],[5,6]]
D=[[1,2],[3,4]]
b=[1,2]

from sympy import *

A1=Matrix(A)
B1=Matrix(B)
C1=Matrix(C)
D1=Matrix(D)
b1=Matrix(b)
print_matriz(A)
print_matriz(B)
print_matriz(C)
print_matriz(D)
print_vector(b)
print('---------------------------')
print('El resultado de arriba es el de nosotros, el de abajo es el de sympy')
print('---------------------------')
print('Suma A+B:')
print_matriz(suma(A,B))
print(A1+B1)
print('---------------------------')
print('Resta A-B')
print_matriz(resta(A,B))
print(A1-B1)
print('---------------------------')
print('A*B(transpuesta)')
print_matriz(producto(A,transpuesta(B)))
print(A1*transpose(B1))
print('---------------------------')
print('inversa(D)')
print_matriz(inversa(D))
print(D1**-1)
print('---------------------------')
print('Dx=b')
print('---------------------------')
print_vector(matriz_por_vector(b,inversa(D)))
print((D1**-1)*b1)
print('---------------------------')
print('Determinante D')
print(determinante(D))
print(D1.det())
print('---------------------------')





