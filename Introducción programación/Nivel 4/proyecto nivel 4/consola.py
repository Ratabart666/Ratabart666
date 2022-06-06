import funciones as f

def letraunificada(texto:str)->str:
    '''Unifica la letra ingresada por el usuario a una letra mayúscula y sin tildes.
    Parámetro:
        texto: Texto que se desea unificar.
    Retorno:
        Letra con el formato unificado.'''
    texto=texto.upper()
    texto=texto.replace('Ñ','N')
    texto=texto.replace('Á','A')
    texto=texto.replace('É','E')
    texto=texto.replace('Í','I')
    texto=texto.replace('Ó','O')
    texto=texto.replace('Ú','U')
    return texto
    

def imprimir_menu_principal():
    """ Imprime los items del menú principal de la aplicación.
    """
    print('Analizador datos icfes')
    print('(1) Cargar data Frame y cargar una matriz con la información cruzada de numeros de estudiantes por estrato(Estrato 1,Estrato 2,Estrato 3,Estrato 4,Estrato 5,Estrato 6)')
    print('y hábito de lectura(30 minutos o menos,Entre 30 y 60 minutos,Entre 1 y 2 horas,Mas de 2 horas,No leo por entretenimiento )')
    print('(Se muestran diccionarios para interpretar posiciones de la matriz)')
    print('(2) Mostrar distribución de nacionalidad (excepto Colombiana y Venezolana)')
    print('(3) Mostrar distribución de género para un estrato dado')
    print('(4) Mostrar los 10 departamentos con mejor promedio global')
    print('(5) Mostrar los 5 municipios con peor promedio global para un departamento dado')
    print('(6) Mostrar el top de municipios para una categoría dada(Lectura,Matemáticas,Naturales,Sociales,Inglés)')
    print('(7) Mostrar el promedio global por estrato')
    print('(8) Mostrar el promedio para una materia según alimento(Proteínas, Lácteos y Frutos) y su consumo para una categoría dada')
    print('(Lectura,Matemáticas,Naturales,Sociales,Inglés)')
    print('(9) Indica el número de estudiantes que presentaron la prueba para un estrato dado(1,2,3,4,5,6) ')
    print('(10) Indica el número de estudiantes con un hábito de lectura dado')
    print('(11) Indica el estrato que presento el mayor número de pruebas')
    print('(12) Indica el estrato y el hábito de lectura mas común para los estudiantes que presentaron la prueba')
    print('(13) Salir de la aplicación')
    print('-----------------------------------------------------------------------------')

def cargar_datos()->tuple:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de las pruebas icfes.
        Retorno:
            El DataFrame con la información de las pruebas icfes.
    """
    print('Cargar datos(Dataframe y matriz)')
    archivo=input("Por favor ingrese el nombre del archivo CSV con las pruebas icfes: ")
    datos=f.cargar_datos(archivo)
    if len(datos)==0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información de la asistencia.")
    else:
        tupla=f.crear_matriz(datos)
        matriz=tupla[0]
        estrato=tupla[1]
        lectura=tupla[2]
        print('DataFrame')
        print(datos)
        print('Matriz información lectura')
        for dato in matriz:
            print(dato)
        print('Diccionario estrato (filas)')
        print(estrato)
        print('Diccionario habito lectura (columna)')
        print(lectura)
        
        
        
        print("Se cargaron los datos del icfes(Data frame y matriz) a partir del anterior archivo.")
        print('-----------------------------------------------------------------------------')
    return (datos,tupla)

def ejecutar_nacionalidad(tupla:tuple)->None:
    """Ejecuta la función nacionalidad de la libreria importada 'funciones'.
        
    """
    f.nacionalidad(tupla[0])
    print('-----------------------------------------------------------------------------')


def ejecutar_generoestrato(tupla:tuple)->None:
    """solicita al usuario que ingrese el estrato a analizar, con este dato ejecuta la función
    generoestrato de la libreria importada 'funciones' .       
    """
    
    estrato=input('Ingrese el estrato deseado(1,2,3,4,5,6): ')
    if estrato=='1' or estrato=='2' or estrato=='3' or estrato=='4' or estrato=='5' or estrato=='6':
        f.generoestrato(tupla[0],estrato)
        print('-----------------------------------------------------------------------------')

    else:
        print('Porfavor ingrese un estrato válido(1,2,3,4,5,6)')
        print('-----------------------------------------------------------------------------')

    
def ejecutar_desempenoalto(tupla:tuple)->None:
    """Ejecuta la función desempenoalto de la libreria importada 'funciones'.
        
    """
    f.desempenoalto(tupla[0])
    print('-----------------------------------------------------------------------------')


def ejecutar_desempenobajo(tupla:tuple)->None:
    """solicita al usuario que ingrese el departamento a analizar, con este dato ejecuta la función
    desempenobajo de la libreria importada 'funciones' .       
    """
    
    departamento=input('Ingrese el departamento deseado a analizar:  ')
    departamento=letraunificada(departamento)
    departamentos=tupla[0]['DEPARTAMENTO'].unique()
    validacion=departamento in departamentos
    if validacion==True:
        f.desempenobajo(tupla[0],departamento)
        print('-----------------------------------------------------------------------------')

    else:
        print('Ingrese un departamento válido')
        print(sorted(departamentos))
        print('-----------------------------------------------------------------------------')


def ejecutar_top(tupla:tuple)->None:
    """solicita al usuario que ingrese una asignatura 
    (Lectura,Matemáticas,Naturales,Sociales,Inglés)a analizar, con este dato ejecuta la función
    top de la libreria importada 'funciones' .       
    """
    categoria=input('Ingrese una categória(Lectura,Matemáticas,Naturales,Sociales,Inglés): ')
    categoria=letraunificada(categoria)
    if categoria=='LECTURA' or  categoria=='MATEMATICAS' or categoria=='NATURALES' or categoria=='SOCIALES' or categoria=='INGLES':
        f.top(tupla[0],categoria)
        print('-----------------------------------------------------------------------------')

    else:
        print('Ingrese una categória válida(Lectura,Matemáticas,Naturales,Sociales,Inglés): ')
        print('-----------------------------------------------------------------------------')

        
def ejecutar_estratos(tupla:tuple)->None:
    """Ejecuta la función estratos de la libreria importada 'funciones'.
        
    """
    f.estratos(tupla[0])
    print('-----------------------------------------------------------------------------')


def ejecutar_nutricion(tupla:tuple)->None:
    """solicita al usuario que ingrese una asignatura 
    (Lectura,Matemáticas,Naturales,Sociales,Inglés)a analizar y un alimento(Proteínas, Lácteos y Frutos)
    con este dato ejecuta la función nutricion de la libreria importada 'funciones'.      
    """
    alimento=input('Ingrese un alimento(Proteínas, Lácteos y Frutos): ')
    categoria=input('Ingrese una categória(Lectura,Matemáticas,Naturales,Sociales,Inglés): ')
    categoria=letraunificada(categoria)
    alimento=letraunificada(alimento)
    if (categoria=='LECTURA' or  categoria=='MATEMATICAS' or categoria=='NATURALES' or categoria=='SOCIALES' or categoria=='INGLES') and (alimento=='PROTEINAS' or alimento=='LACTEOS' or alimento=='FRUTOS'):
        f.nutricion(tupla[0],alimento,categoria)
        print('-----------------------------------------------------------------------------')

    else:
        print('Ingrese un alimento valido(Proteínas, Lácteos y Frutos) junto con una categoria válida(Lectura,Matemáticas,Naturales,Sociales,Inglés)')
        print('-----------------------------------------------------------------------------')


def ejecutar_pruebaestrato(tupla:tuple)->None:
    """solicita al usuario que ingrese un estrato (1,2,3,4,5,6) a analizar, con este dato ejecuta la función
    pruebaestrato de la libreria importada 'funciones'.       
    """
    
    estrato=input('Ingrese el estrato deseado(1,2,3,4,5,6): ')
    if estrato=='1' or estrato=='2' or estrato=='3' or estrato=='4' or estrato=='5' or estrato=='6':
        total=f.pruebaestrato(tupla[1][0],estrato)
        print(str(total)+' estudiantes de estrato '+estrato+' presentarón la prueba')
        print('-----------------------------------------------------------------------------')
   
    else:
        print('Ingrese un estrato valido(1,2,3,4,5,6)')
        print('-----------------------------------------------------------------------------')

        
    


def ejecutar_estudianteslectura(tupla:tuple)->None:
    """solicita al usuario que ingrese un hábito de lectura a analizar:
        (1)Entre 30 minutos o menos
        (2)Entre 30 y 60 minutos
        (3)Entre 1 y 2 horas
        (4)Más de 2 horas
        (5)No leo por entretenimiento
        
    Con este dato ejecuta la función
    estudianteslectura de la libreria importada 'funciones'.       
    """
    print('(1)Entre 30 minutos o menos')
    print('(2)Entre 30 y 60 minutos')
    print('(3)Entre 1 y 2 horas')
    print('(4)Más de 2 horas')
    print('(5)No leo por entretenimiento')
    salir=False
    lectura=input('Ingrese el hábito de lectura: ')
    if lectura=='1' or lectura=='2' or lectura=='3' or lectura=='4' or lectura=='5':
        total=f.estudianteslectura(tupla[1][0],tupla[1][2][int(lectura)-1])
        print('El número de estudiantes con la lectura establecida es '+str(total))
        print('-----------------------------------------------------------------------------')
    else:
        while salir==False:
            print('Ingrese una opción valida')
            print('(1)Entre 30 minutos o menos')
            print('(2)Entre 30 y 60 minutos')
            print('(3)Entre 1 y 2 horas')
            print('(4)Más de 2 horas')
            print('(5)No leo por entretenimiento') 
            print('-----------------------------------------------------------------------------')
            



def ejecutar_mayorestrato(tupla:tuple)->None:
    """Ejecuta la función mayor estrato de la libreria importada 'funciones'.
        
    """
    estmax=f.mayorestrato(tupla[1][0])
    print('El estrato '+estmax+' presentó la mayoria de las pruebas')
    print('-----------------------------------------------------------------------------')


def ejecutar_mayorestratotiempolec(tupla:tuple)->None:
    """Ejecuta la función mayorestratotiempolec de la libreria importada 'funciones'.
        
    """
    inf=f.mayorestratotiempolec(tupla)
    estrato=inf[0]
    lectura=inf[1]
    print('La mayoria de los estudiantes que presentaron la prueba pertenecen a '+estrato+' y tienen un hábito de lectura de: '+lectura)
    print('-----------------------------------------------------------------------------')


def iniciar_aplicacion():
    salir=False
    tupla=cargar_datos() 
    while salir==False: 
        imprimir_menu_principal()
        opcion=input("Ingrese la opción deseada: ")

        if opcion=='1':
            print('Cargar datos(Dataframe y matriz)')
            print('-----------------------------------------------------------------------------')
            tupla=cargar_datos()
        elif opcion=='2':       
            ejecutar_nacionalidad(tupla)
        elif opcion=='3':
            ejecutar_generoestrato(tupla)
        elif opcion=='4':
            ejecutar_desempenoalto(tupla)
        elif opcion=='5':
            ejecutar_desempenobajo(tupla)
        elif opcion=='6':
            ejecutar_top(tupla)
        elif opcion=='7':
            ejecutar_estratos(tupla)
        elif opcion=='8':
            ejecutar_nutricion(tupla)
        elif opcion=='9':
            ejecutar_pruebaestrato(tupla)
        elif opcion=='10':
            ejecutar_estudianteslectura(tupla)
        elif opcion=='11':
            ejecutar_mayorestrato(tupla)
        elif opcion=='12':
            ejecutar_mayorestratotiempolec(tupla[1])
        elif opcion=='13':
            salir=True
        else:
            print("El valor ingresado no es válido.")
            print('-----------------------------------------------------------------------------')

iniciar_aplicacion()    
        
    


    
