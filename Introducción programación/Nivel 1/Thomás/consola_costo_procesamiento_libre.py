import calculadora_aws as calc
def ejecutar_calculadora_costo_procesamiento_libre()->None:
    Dedicados_libre= int(input('El número de servidores dedicados libre en el mes fueron:'))
    Compartidos_libre= int(input('El número de servidores dedicados libre en el mes fueron:'))
    Costo=float(input('El costo de un servidor dedicado por hora es:'))
    Resultado= calc.costo_procesamiento_libre(Dedicados_libre,Compartidos_libre,Costo)
    print(Resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de costo de procesamiento libre mensual')
    ejecutar_calculadora_costo_procesamiento_libre()
    

iniciar_aplicación()

