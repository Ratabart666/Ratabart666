def cargar_datos(nombre_archivo: str,encoding='utf-8') -> list:
    
    lista_congresistas = list()
    datos_congresista = dict()
    with open(nombre_archivo, encoding='utf-8') as archivo:
        archivo.readline()
        linea = archivo.readline()
        while len(linea) > 0:
            datos = linea.split(",")
            congresista = datos_congresista.get("nombre")
            if congresista == datos[0]:
                if datos[4] == "plenaria":
                    datos_congresista["asistencia_plenaria"][datos[3]] = datos[5].strip()
                else:
                    datos_congresista["asistencia_congreso_pleno"][datos[3]] = datos[5].strip()
            else:
                if congresista != None:
                    lista_congresistas.append(datos_congresista)

                if datos[4] == "plenaria":
                    datos_congresista = {
                        "nombre": datos[0], "movimiento": datos[1], "circunscripcion": datos[2],
                        "asistencia_plenaria": {datos[3]: datos[5].strip()}, "asistencia_congreso_pleno":{}}
                else:
                    datos_congresista = {
                        "nombre": datos[0], "movimiento": datos[1], "circunscripcion": datos[2],
                        "asistencia_plenaria": {}, "asistencia_congreso_pleno": {datos[3]: datos[5].strip()}}
            linea = archivo.readline()

    archivo.close()
    return lista_congresistas
lista=cargar_datos('asistencia_congreso.csv')


def buscar_congresista_por_nombre(nombre:str, lista:list)->dict:
    """ (15%) Retorna el diccionario del congresista con el nombre dado por parámetro, 
    Si no existe un congresista con el nombre dado, retorna None
        """
    respuesta=None
    for diccionario_congresista in lista:
        nombre_=diccionario_congresista['nombre']
        if nombre==nombre_:
            respuesta=diccionario_congresista
    
    return respuesta

def dar_congresistas_por_movimiento(nombre_movimiento:str, lista:list)->list:
    """ (20%) Retorna una lista con los congresistas que pertenecen al movimiento político dado por 
    paámetro. Si no hay congresistas que pertenezcan a ese movimiento político, retorna una
    lista vacía.
    En cada posición de la lista, debe haber un diccionario con toda la información del congresista. 
    """
    lista2=[]
    movimiento_congresista=''
    for congresista in lista:
        movimiento_congresista=congresista['movimiento']
        if movimiento_congresista==nombre_movimiento:
            lista2.append(congresista['nombre'])
   
    return lista2


def dar_movimientos_politicos(lista:list)->dict: 
    """ (30%) Retorna un diccionario donde las llaves son el nombre del movimiento político, y el valor
    el número de congresistas que pertencen a este. ej:
        {'CENTRO DEMOCRATICO': 34, 'COLOMBIA JUSTA LIBRES': 1, 'CAMBIO RADICAL': 32, 'FARC': 7 ...}
        """
    
   
    dic={}
    dic2={}
    for i in lista :
         x=i['movimiento']
         dic[x]=0
    lista2=dic.keys()
    lista2=sorted(lista2)
    for i in lista2:
        dic2[i]=0
    for i in lista:
        x=i['movimiento']
        dic2[x]+=1
    
   

        

        
        
    
    
    return dic2
 

def congresista_menos_asistencias_plenarias_congreso(lista:list)->dict:
    """ (35%) Retorna un diccionario con la siguiete estructura: 
       {'nombre':'Nombre congresista', 'asistencias':#asistencias}
        donde Nombre congresista es el nombre del congresista que menos asistió a la suma de 
        asistencias de plenaria y congreso pleno unificados y #asistencias es el número de asistencias que 
        tuvo entre las dos.
        """
    c=0
    a=lista[0]['asistencia_plenaria']
    b=lista[0]['asistencia_congreso_pleno']
    menor=0
    for j in a:
             if a[j]=='ASISTIÓ':
                 menor+=1
    for j in b:
             if b[j]=='ASISTIO':
                 menor+=1 
    congresista={}
    for i in lista:
        x=i['asistencia_plenaria']
        y=i['asistencia_congreso_pleno']
        for j in x:
             if x[j]=='ASISTIÓ':
                 c+=1
        for j in y:
             if y[j]=='ASISTIÓ':
                 c+=1 
        if c<menor:
                 congresista=i
                 menor=c
        c=0
        
    
    
    return congresista
print(congresista_menos_asistencias_plenarias_congreso(lista))


def iniciar_aplicacion()->None:
    lista = cargar_datos('asistencia_congreso.csv')

       
iniciar_aplicacion()