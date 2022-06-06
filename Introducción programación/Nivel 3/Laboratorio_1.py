def pum(x:int,jugadores:int)->str:
    c=1
    a=1
    while c<=14:
        if a==jugadores+1:
            a=1
        if c%x==0:
            print(a,'Pum')
        else:
            print(a,c)
        a+=1
        c+=1
    return 'Se ha terminado el juego'



def sucesion_fibonacci(x:int)->str:
    número_final_termino=1
    número_inicial_termino=0
    número_serie=1
    print(0)
    print(1)
    while número_serie<x-1:
        número_serie+=1
        suma=número_inicial_termino+número_final_termino
        número_inicial_termino=número_final_termino
        número_final_termino=suma  
        print(suma)
    return 'Se ha imprimido la sucesión deseada' 
        
            
                  
    

        

            
            
        
    
    
    


