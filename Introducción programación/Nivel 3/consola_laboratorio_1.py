import Laboratorio_1 as mod

def menu():
    print('Bienvenido, elija una opcion: ')
    print('1) Jugar al pum')
    print('2) Sucesion de fibonacci')
    print('#)Salir')
    x=input('Elija una opcion: ')
    y=None
    z=None
    if x=='1':
        y=int(input('Elija el numero de inicio: '))
        z=int(input('Elija la cantidad de jugadores: '))
        print('Jugador,Jugada')
        print(mod.pum(y,z))
        menu()
    elif x=='2':
        y=int(input('Elija la cantidad de terminos que desea ver: '))
        print(mod.sucesion_fibonacci(y))
        menu()
    elif x=='#':
        print('Gracias')
    else:
        print('Ingrese input valido')
        menu()
menu()
        
    