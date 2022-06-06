import calculadora_aws as calc
def ejecutar_calculadora_tiempo_transferencia()->None:
    Tamano= float(input('El tamano en GB del archivo es:'))
    Ancho_banda= int(input('El ancho de banda en Mb/s es:'))
    Resultado= calc.tiempo_transferencia(Tamano,Ancho_banda)
    print(Resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de tiempo de transferencia')
    ejecutar_calculadora_tiempo_transferencia()
    
iniciar_aplicación()

    




