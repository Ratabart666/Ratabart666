def crear_estudiante(nom: str, cod: str, gen: str, carr: str, prom: float, ssc: float)->dict:
    dic_estudiante = { "nombre": nom, 
                       "código": cod, 
                       "género": gen, 
                       "carrera": carr, 
                       "promedio": prom, 
                       "ssc": ssc}
    return dic_estudiante

#PROGRAMA PRINCIPAL
estudiante1 = crear_estudiante("Juan Pérez", "201824736", "masculino", "Biología", 3.78, 0.7)
estudiante2 = crear_estudiante("Ana Gavalda", "201724736", "femenino", "Ciencias Políticas", 4.25, 3.5)
estudiante3 = crear_estudiante("Bastien Bosa", "201815217", "masculino", "Economía", 3.21, 2.3)
estudiante4 = crear_estudiante("Catalina Gómez", "201715400", "femenino", "Arte", 3.8, 4)


    
def mayor_promedio(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:int)->dict:
        a= max(estudiante1['promedio'],estudiante2['promedio'],estudiante3['promedio'],estudiante4['promedio'])
        if estudiante1['promedio']==estudiante2['promedio'] or estudiante1['promedio']==estudiante3['promedio'] or estudiante1['promedio']==estudiante4['promedio']:
            x={'Hay 2 o mas estudiantes con el mismo promedio'}
        elif estudiante1['promedio']==a:
            x=estudiante1
        elif estudiante2['promedio']==a:
            x=estudiante2
        elif estudiante2['promedio']==a:
            x=estudiante2
        elif estudiante2['promedio']==a:
            x=estudiante2
        return x
def cuantas_mujeres(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:int)->str:
    x=0
    y=0
    z=0
    w=0
    
    if estudiante1['género']=='femenino':
        x=1
    if estudiante2['género']=='femenino':
        y=1
    if estudiante3['género']=='femenino':
        z=1
    if estudiante4['género']=='femenino':
        w=1
    a=x+y+z+w
    return str('El número de mujeres es ')+str(a)
def hay_pila(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:int)->bool:
    x=False
    if estudiante1['promedio']>=4 and estudiante1['género']=='femenino':
        x=True
    elif estudiante2['promedio']>=4 and estudiante2['género']=='femenino': 
        x=True
    elif estudiante3['promedio']>=4 and estudiante3['género']=='femenino': 
        x=True
    elif estudiante4['promedio']>=4 and estudiante4['género']=='femenino': 
        x=True
    return x
def quienes_en_riesgo(estudiante1:dict,estudiante2:dict,estudiante3:dict,estudiante4:int)->dict:   
    r=str('')
    t=str('')
    u=str('')
    i=str('')
    if estudiante1['promedio']<3.4:
        x=estudiante1['promedio']  
        a=estudiante1['código']
        r={a,x}
    if estudiante2['promedio']<3.4:
        y=estudiante2['promedio']
        b=estudiante2['código']
        t={b,y}
    if estudiante3['promedio']<3.4:
        z=estudiante3['promedio']
        c=estudiante3['código']
        u={c,z}
    if estudiante4['promedio']<3.4:
        w=estudiante4['promedio']
        d=estudiante4['código']
        i={d,w}
    return r,t,u,i
print(quienes_en_riesgo(estudiante1, estudiante2, estudiante3, estudiante4))

def existe_estudiante(estudiante1, estudiante2, estudiante3, estudiante4, nombre)->bool:
    x=nombre.lower()
    y= estudiante1["nombre"].lower()
    z= estudiante2["nombre"].lower()
    w= estudiante3["nombre"].lower()
    d= estudiante4["nombre"].lower()
    u=False
    if x== y:
        u= True
    elif x==z :
        u=True
    elif x==w :
        u=True
    elif x==d :
        u= True
    return u

 




    
