import calculadora_aws as calc
def ejecutar_calculadora_tiempo_transferencia()->None:
    Datos= float(input('El número de datos en GB en el mes fueron:'))
    Porcentaje_aws= float(input('El porcentaje de datos transferidos por AWS en el mes fueron:'))
    Resultado= calc.costo_transferencia(Datos,Porcentaje_aws)
    print(Resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de costo transferencia mensual')
    ejecutar_calculadora_tiempo_transferencia()


iniciar_aplicación()

    
    

    
    

