import calculadora_aws as calc
def ejecutar_calculadora_costo_almacenamiento()->None:
    Lectura=int(input('El número de solicitudes de lectura en el mes fueron:'))
    Escritura=int(input('El número de solicitudes de escritura en el mes fueron:'))
    Almacenamiento=int(input('El tamaño en GB almacenado en el mes son:'))
    resultado= calc.costo_almacenamiento(Lectura,Escritura,Almacenamiento)
    print(resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de costo de almacenamiento mensual')
    ejecutar_calculadora_costo_almacenamiento()   

iniciar_aplicación()

