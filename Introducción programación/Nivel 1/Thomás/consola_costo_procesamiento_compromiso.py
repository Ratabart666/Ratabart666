import calculadora_aws as calc
def ejecutar_calculadora_costo_procesamiento_compromiso()->None:
    Dedicados_compromiso= int(input('El número de servidores dedicados compromiso es:'))
    Compartidos_compromiso= int(input('El número de servidores dedicados compromiso es:'))
    Costo=float(input('El costo de un servidor dedicado por hora es:'))
    Resultado= calc.costo_procesamiento_compromiso(Dedicados_compromiso,Compartidos_compromiso,Costo)
    print(Resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de costo de procesamiento compromiso mensual')
    ejecutar_calculadora_costo_procesamiento_compromiso()
    

iniciar_aplicación()


