#Por comodida y para realizar el mínimo de subfunciones todas las funciones estan en función de la lista_congreso


def cargar_archivo(archivo:str)->list:#1
    '''Esta función organiza los datos del archivo csv del congreso através del retorno de una lista
    que tiene como información los diccionarios de cada congresista, los diccionarios de
    cada congresista tienen como llave: nombre,movimiento,circunscripción,asistencia.Este
    último tiene como valor un diccionario que tiene como llaves la fecha de asistencia y como valor la información de asistencia
    Parámetros:
        archivo(str):Corresponde al nombre del archivo que contiene la información del congreso
    Retorno:
        Retorna una lista con la información de cada congresista'''
    
    data=open(archivo,'r',encoding='utf-8')
    lista_madre=[]
    lista_congreso=[]
    line=data.readline()
    c=0
    d=0
    while line!='':
        line=data.readline()
        lista=line.split(',')
        lista_madre.append(lista)
    
        
    for n in range(0,len(lista_madre)):
        if lista_madre[n][0]!=lista_madre[n-1][0]:
            c=d
            d=n
            if d!=0:
                lista_congreso=diccionario(lista_madre, lista_congreso,c,d)
    data.close()
    return lista_congreso  
def formato_fechas(fecha:str)->str:
    """
    Pone en formato simple las fechas que se le pasen por parámetro.

    Parámetros:
        fecha (str) fecha en formato dd/mm/aaaa
        
    Retorno:
        Un string en formato unificado. Ejemplo 7/8/20
    """

    lista = fecha.split("/")

    if lista[0][0] == '0':
        lista[0] = lista[0][1:]

    if lista[1][0] == '0':
        lista[1] = lista[1][1:]

    if len(lista[2]) ==4:
        lista[2] = lista[2][2:]

    respuesta= "{}/{}/{}".format(lista[0],lista[1], lista[2])
    return respuesta              
def diccionario(lista_madre:list,lista_congreso:list,inferior:int,superior:int)->list:#subfunción de cargar_archivo
    ''''Subfunción encargada de crear el diccionario correspondiente a cada congresista,tiene como parámetros una listamadre(lista con información bruta y sin organizar)
    Parámetros:
        listamadre(list):Lista con la información de cada linea del archivo csv
        lista_congreso(list):Lista con la información organizada
        inferior(int):Número de la lista en la cual se inicia un nuevo congresista
        superior(int):Número de la lista donde inicia el congresista siguiente
    Retorno:
        Retorna la lista del congreso con la información de un nuevo congresista'''
        
    diccionariocongresista={}
    diccionarioasistencia={}
    contador=inferior
    diccionariocongresista['nombre']=lista_madre[inferior][0]
    diccionariocongresista['movimiento']=lista_madre[inferior][1]
    diccionariocongresista['circunscripción']=lista_madre[inferior][2]
    while contador<superior:
        diccionarioasistencia[formato_fechas(lista_madre[contador][3])]=lista_madre[contador][4].replace('\n','')
        contador+=1
    diccionariocongresista['asistencia']=diccionarioasistencia
    lista_congreso.append(diccionariocongresista)
    return lista_congreso
#Las fuciones cargar archivo solo son validas en un archivo csv creado de manera correta.Ademas todos los datos deben estar en orden cronologíco      

def congresista_con_mas_fallas_injustificadas(listacongreso:list)->str:#2
    '''Esta función tiene como parámetro la lista con la información del congreso, esta misma retorna el congresista
    con más fallas injustificadas('SIN EXCUSA')
    Párametros:
        listacongreso(list): Lista organizada con información del congreso
    Retorno:
        Retorna el congresista con más fallas injustificadas a través de un str'''
    mayor=0
    c=0
    congresista=''
    for i in listacongreso :
         x=i['asistencia']
         for j in x:
             if x[j]=='SIN EXCUSA':
                 c+=1
         if c>mayor:
                 congresista=i['nombre']
                 mayor=c 
         c=0
    return ('El congresista '+congresista+' faltó '+str(mayor)+' veces a sesiones de forma injustificada')
    

     
     
 

def congresista_mayor_asistencia(listacongreso:list)->str:#3
     '''Esta función tiene como parámetro la lista con la información del congreso y retorna el congresista
     con mayor asistencia
    
    Parámetros:
        listacongreso(list):Lista organizada con información del congreso
    Retorno:
        Retorna el congresista con más asistencias a través de un str'''

     c=0
     mayor=0
     congresista=''
     for i in listacongreso :
         x=i['asistencia']
         for j in x:
             if x[j]=='ASISTIÓ':
                 c+=1
         if c>mayor:
                 congresista=i['nombre']
                 mayor=c
         c=0
     return ('El congresista con mayor asistencias es '+congresista+' con un total de '+str(mayor)+' asistencias')

def diccionario_2(nombre:str,porcentaje:float)->dict:#subfunción porcentaje_asistencia
    '''Esta subfunción tiene como parámetros el nombre de un congresista y su porcentaje de asistencia y retorna un diccionario
    con esta información
    Parámetros:
        nombre(str):Nombre congresista
        porcentaje(float):Porcentaje de asistencia
    Retorno:
        Diccionario con llave igual al nombre del congresista y valor igual al porcentaje'''
    dic={}
    dic['nombre']=nombre
    dic['porcentaje de asistencia']=porcentaje
    return dic
 
def porcentaje_asistencia(listacongreso:list)->list:#4
    '''Esta función tiene como parámetro la lista de la infomación del congreso y retorna el porcentaje de asistencia de cada congresista
    Parámetros:
        Listacongreso(list)=Lista organizada con información del congreso
    Retorno:
        Lista cuyos valores son diccionarios con llaves igual al nombre del congresista y valores igual a su porcentaje de asistencia'''
    
    lista=[]
    asistio=0
    porcentaje=0
    
    
    for i in listacongreso:
        x=i['asistencia']
        nombre=i['nombre']
        for j in x:
            if x[j]=='ASISTIÓ':
                asistio+=1  
        porcentaje=round((asistio/len(x)),2)
        y=diccionario_2(nombre,porcentaje)
        lista.append(y)
        asistio=0
    return lista


def circunscripciones(listacongreso:list)->dict:#subfunción circunscripciones_con_mas_fallas y asistencia_por_circunscripcion_por_mes_y_año_determinados
    '''Subfunción encargada de retonar una lista que tiene como valores las circunscripciones,tiene como parámetro la lista organizada del congreso
     Parámetro:
         Listacongreso(list)=Lista organizada con información del congreso
     Retorno:
         Lista con valores igual a las circunscripciones(La lista esta organizada en orden alfabetico)'''

    dic={}
    dic2={}
    for i in listacongreso :
         x=i['circunscripción']
         dic[x]=0
    lista=dic.keys()
    lista=sorted(lista)
    for i in lista:
        dic2[i]=0
    return dic2
    
        
def circunscripción_con_mas_fallas(listacongreso:list)->str:#5
    '''Esta función tiene como parámetro la lista con la información del congreso, esta misma retorna la circunscripción
    con más fallas
    Párametros:
        listacongreso(list): Lista organizada con información del congreso
    Retorno:
        Retorna la circunscripción con más fallas a través de un str'''
    diccircunscripciones=circunscripciones(listacongreso)
    c=''
    for i in listacongreso:
            x=i['asistencia']
            y=i['circunscripción']
            for j in x:
                if x[j]!='ASISTIÓ':
                    diccircunscripciones[y]+=1
    a=max(diccircunscripciones.values())
    for i in diccircunscripciones:
        if diccircunscripciones[i]==a and c=='':
            c=i
    return ('La circunscripción '+c+' acumuló '+str(a)+' fallas.')

def congresista_con_mas_excusas_medidas(listacongreso:list)->str:#6
    '''Esta función tiene como parámetro la lista con la información del congreso, esta misma retorna el congresista
    con más fallas medicas('EX. MÉDICA')
    Párametros:
        listacongreso(list): Lista organizada con información del congreso
    Retorno:
        Retorna el congresista con más fallas medicas('EX. MÉDICA') a través de un str'''
    c=0
    mayor=0
    congresista=''
    for i in listacongreso :
         x=i['asistencia']
         for j in x:
             if x[j]=='EX. MÉDICA':
                 c+=1
         if c>mayor:
                 congresista=i['nombre']
                 mayor=c
         c=0
    return ('El congresista '+congresista+' falló '+str(mayor)+' veces con excusa médica')

def congresista_que_fallan_n_veces(listacongreso:list,numero_de_fallas:int)->dict:#7
     '''Función que tiene como parámetro la lista del congreso y un número deseado de fallas,esta misma retorna un 
    diccionario con los congresistas que faltaron mas de el número deseado de fallas y su correspondiente falla
    Parámetros:
        listacongreso(list): Lista organizada con información del congreso
        numero_de_fallas(int): Corresponde al número deseado de fallas a comparar
    Retorno:
        Retorna un diccionario con llave igual al nombre del congresista que faltó mas del número deseado de veces y como llave el número de fallas, si todos
        si todos los congresistas faltaron menos veces que la deseada retorna('Todos los congresistas tuvieron menos fallas que la ingresada')
'''

     dic={}
     noasistio=0
     for i in listacongreso:
        x=i['asistencia']
        nombre=i['nombre']
        for j in x:
            if x[j]!='ASISTIÓ' and x[j]!='SILLA VACÍA' and x[j]!='SUSPENSIÓN':
                noasistio+=1
        if noasistio>numero_de_fallas:
            dic[nombre]=noasistio
        noasistio=0
     if dic=={}:
         dic='Todos los congresistas tuvieron menos fallas que la ingresada'
     return dic
 
def partidos(listacongreso:list)->dict:#subfunción promedio_porcentaje_asistencia_por_partido 
    '''Subfunción encargada de retonar un diccionario que tiene como valores los partidos políticos,tiene como parámetro la lista organizada del congreso
     Parámetro:
         Listacongreso(list)=Lista organizada con información del congreso  
     Retorno:
         Diccionario con llaves igual a los partidos políticos(El diccionario esta organizada en orden alfabetico) y valores igual a 0'''
    
    dic={}
    dic2={}
    for i in listacongreso :
         x=i['movimiento']
         dic[x]=0
    lista=dic.keys()
    lista=sorted(lista)
    for i in lista:
        dic2[i]=0
    return dic2

def promedio_porcentaje_asistencia_por_partido(listacongreso:list)->dict:#8
     '''Función encargada de retornar el porcentaje(0-1) de asistencia de los congresistas, tiene como parámetro la lista 
    del congreso organizada
    Parámetro:
        Listacongreso(list)=Lista organizada con información del congreso
    Retorno:
        Diccionario con llaves igual a los partidos politicos y valores iguales a su porcentaje de asistencia'''

        
     dicasistencia=partidos(listacongreso)
     dicfallas=partidos(listacongreso)
     dic=partidos(listacongreso)
     for i in listacongreso:
         x=i['asistencia']
         partido=i['movimiento']
         for j in x:
             if x[j]=='ASISTIÓ':
                 dicasistencia[partido]+=1
             elif x[j]=='SUSPENSIÓN' or x[j]=='SILLA VACÍA':
                 dicasistencia[partido]+=0                
             else:
                 dicfallas[partido]+=1
     for i in dic:
         dic[i]=round((dicasistencia[i])/(dicasistencia[i]+dicfallas[i]),2)
     return dic

def fechas(listacongreso:list)->dict:#subfunción fecha_con_mas_fallas
    '''Funcíon que retorna todas las fechas de sesiones del congreso, esta función tiene como parámetro la lista organizada del congreso
    Parámetros:
        listacongreso(list):Lista organizada con información del congreso
    Retorno:
        Diccionario con valores iguales a las fechas de las sesiones del gobierno y valores igual a 0'''
    dic={}
    dic2={}
    for i in listacongreso :
         x=i['asistencia']
         for j in x:
             dic[j]=0
    lista=dic.keys()
    for i in lista:
        dic2[i]=0
    return dic2

def fecha_con_mas_fallas(listacongreso:list)->dict:#9
    '''Función que retorna la fecha donde existieron más fallas a las sesiones del congreso,
    tiene como parámetro la lista organizada del congreso
    Parámetros:
        listacongreso(list):Lista organizada con información del congreso
    Retorno:
        Retorna la fecha donde existieron más fallas al congreso a través de un str'''

    dicfechas=fechas(listacongreso)
    c=''
    for i in listacongreso:
            x=i['asistencia']
            for j in x:
                if x[j]!='ASISTIÓ':
                    dicfechas[j]+=1
    a=max(dicfechas.values())
    for i in dicfechas:
        if dicfechas[i]==a and c=='':
            c=i
    return ('En la fecha '+c+' hubo '+str(a)+' fallas.')

def mes_año(listacongreso:list)->dict:#subfunción mes_con_mayor_numero_de_sesiones
    '''Subfunción encargada de retornar todas los meses de cada año de las sesiones del congreso,
    tiene como parámetro la lista organizada del congreso
    Parámetros:
        lista(congreso):Lista organizada con información del congreso
    Retorno:
        Retorna un diccionario con valores iguales a los meses junto a cada año de las sesiones,
        el valor de todas las llaves es 0'''
    dic={}
    mes=''
    año=''
    for i in listacongreso :
         x=i['asistencia']
         for j in x:
             j=j.split('/')
             mes=j[1]
             año=j[2]
             j=mes+'/'+año
             
             dic[j]=0  
    return dic

def mes_dia_año(listacongreso:list)->dict:#subfunción mes_con_mayor_numero_de_sesiones
    '''Subfunción encargada de retornar todas las fechas de las sesiones del congreso,
    tiene como parámetro la lista organizada del congreso
    Parámetros:
        lista(congreso):Lista organizada con información del congreso
    Retorno:
        Retorna un diccionario con valores iguales a las fechasde las sesiones del congreso
        y el valor de todas las llaves es 0'''
    dic={}
    for i in listacongreso :
         x=i['asistencia']
         for j in x:
             dic[j]=0
    return dic



    
        
def mes_con_mayor_numero_de_sesiones(listacongreso:list)->str:#10
    '''Función que retorna el mes junto con el año de ese mismo mes,con mayor sesiones del congreso,tiene como 
    parámetro la lista organizada del congreso
    Parámetro:
        listacongreso(list):Lista organizada con información del congreso
    Retorno:
        El mes junto con el año en el que se realizó mas sesiones al congreso'''
    dicmeses=mes_año(listacongreso)
    dicfecha=mes_dia_año(listacongreso)
    c=''
    mes=''
    año=''
    mesaño=''
    for i in dicfecha:
        i=i.split('/')
        mes=i[1]
        año=i[2]
        mesaño=mes+'/'+año
        dicmeses[mesaño]+=1
              
    a=max(dicmeses.values())
    for i in dicmeses:
        if dicmeses[i]==a and c=='':
            c=i
    return ('En el mes '+c+' hubo '+str(a)+' sesiones.')


def asistencia_congresista_por_fecha_determinada(listacongreso:list,nombre:str,dia:str,mes:str,año:str)->bool:#11
    '''Función encargada de decir si un congresista asistió o no en determinada fecha al congreso
    Parámetros:
        listacongreso(list):Lista organizada con información del congreso
        nombre(str):Nombre en Mayúscula del congresista
        dia(int):día de la fecha deseada
        mes(int):mes de la fecha deseada
        año(int):año de la fecha deseada
    Retorno:
        True si asistió, False si no asistió'''
    r=False  
    fecha=dia+'/'+mes+'/'+año
    for i in listacongreso:
        if i['nombre']==nombre:
            x=i['asistencia']
            for j in x:
                if j==fecha and x[j]=='ASISTIÓ':
                    r=True
    return r

def asistencia_por_circunscripcion_por_mes_y_año_determinados(listacongreso:list,mes:str,año:str)->dict:#12
    '''Función encargada de retornar el número de asistencias de cada circunscripción en un determinado mes
    Parámetros:
        listacongreso(list):Lista organizada con información del congreso
        mes(int):mes de la fecha deseada
        año(int):año de la fecha deseada
    Retorno:
        Diccionario con llaves igual a las circunscripciones y valor igual a su número de asistencias'''
    fecha=mes+'/'+año
    diccir=circunscripciones(listacongreso)
    for i in listacongreso:
        x=i['asistencia']
        circunscripcion=i['circunscripción']
        for j in x:
            temp=j
            j=j.split('/')
            mes=j[1]
            año=j[2]
            j=mes+'/'+año
            if j==fecha and x[temp]=='ASISTIÓ':
                diccir[circunscripcion]+=1
    return diccir

        
            
        

                   


    
    

    

    
    
    
                    
            
         
            
                
            
        
                

    
     
     
     
    

        
            
   


    
            

        
        
        
            
        
    
            
            

                
        
    
    
            
            
            
            




    


        
      
          
          

        
        
        
        


        
       
    

        
        


    
