import calculadora_aws as calc
def ejecutar_calculadora_tiempo_transferencia()->None:
    servidores_compromiso= int(input('El número de servidores en compromiso es:'))
    porcentaje_compartidas_compromiso= float(input('El porcentaje(0-1) de instancias compartidas en compromiso es:'))
    servidores_libres= int(input('El número de servidores libres en el mes fueron:'))
    porcentaje_compartidas_libres= float(input('El porcentaje(0-1) de instancias compartidas libres en el mes fueron:'))
    costo_dedicado=float(input('El costo de un servidor dedicado por hora es:'))
    solicitudes_totales=int(input('El número de solicitudes totales en el mes fueron:'))
    almacenamiento=float(input('El tamaño almacenado en GB en el mes fue:'))
    datos=float(input('El tamaño de datos que se transfirieron en el mes fueron:'))
    porcentaje_aws=float(input('El porcentaje(0-1) de datos que se transfirieron en AWS en el mes fueron:'))
    Resultado= calc.costo_total(servidores_compromiso,porcentaje_compartidas_compromiso,servidores_libres, porcentaje_compartidas_libres,costo_dedicado,solicitudes_totales,almacenamiento,datos,porcentaje_aws)
    
    print(Resultado)
def iniciar_aplicación()->None:
    print('Bienvenido a la calculadora de costo total mensual')
    ejecutar_calculadora_tiempo_transferencia()
    

iniciar_aplicación()

    
