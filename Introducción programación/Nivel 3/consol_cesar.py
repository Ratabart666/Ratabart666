import Codigo_cesar as mod

def menu():
    print('Decifrando codigo cesar:')
    x=input('Ingrese el texto que desea decifrar: ')
    y=int(input('Ingrese el corrimiento del codigo: '))
    print(mod.descifrar_codigo_cesar(x,y))
    menu()
menu()