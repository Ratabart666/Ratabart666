# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:34:45 2022

@author: Asus
"""
from automata.pda.dpda import DPDA
from automata.pda.npda import NPDA
from automata.tm.dtm import DTM
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


npda1 = NPDA(
    states={"qloop", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "qfinal"},
    input_symbols={"0", "1"},
    stack_symbols={"S", "A", "B", "0", "1", "$"},
    transitions={
        #############################################
        #############################################
        #############################################
        # Se agrega S y $
        "q1": {
            "": {"$": {("qloop", ("S", "$"))}},
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 1
        "q2": {
            "": {"A": {("qloop", ("1", "A"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 2
        "q3": {
            "": {"B": {("qloop", ("0", "B"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 5
        "q4": {
            "": {"S": {("qloop", ("0", "S"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 6
        "q5": {
            "": {"S": {("qloop", ("1", "S"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Medio loop 7
        "q6": {
            "": {"A": {("q7", ("A", "A"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 7
        "q7": {
            "": {"A": {("qloop", ("1", "A"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Medio loop 8
        "q8": {
            "": {"B": {("q9", ("B", "B"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        # Fin loop 8
        "q9": {
            "": {"B": {("qloop", ("0", "B"))}},
            # --------------------------------------------
        },
        #############################################
        #############################################
        #############################################
        "qloop": {
            "": {
                # inicio loop 1,#inicio loop 2,
                "S": {
                    ("q2", "A"),
                    ("q3", "B"),
                },
                # inicio y fin loop 3,inicio loop 5, inicio loop 7
                "A": {
                    ("qloop", "0"),
                    ("q4", "S"),
                    ("q6", "A"),
                },
                # inicio y fin loop 4,inicio loop 6,inicio loop 8
                "B": {
                    ("qloop", "1"),
                    ("q5", "S"),
                    ("q8", "B"),
                },
                "$": {
                    ("qfinal", ""),
                },
            },
            "0": {
                "0": {
                    ("qloop", ""),
                },  # quitar 0's
            },
            "1": {
                "1": {
                    ("qloop", ""),
                },  # quitar 1's
            },
        },
    },
    #############################################
    #############################################
    #############################################
    initial_state="q1",
    initial_stack_symbol="$",
    final_states={"qfinal"},
)

dpda2 = DPDA(
    states={"q2", "q3", "q4", "q5"},
    input_symbols={"0", "1"},
    stack_symbols={"A", "B", "$"},
    transitions={
        #############################################3
        "q2": {"0": {"$": ("q3", ("A", "$"))}},
        #############################################3
        "q3": {
            "0": {"A": ("q3", ("A", "A"))},
            "1": {"A": ("q4", "")}
            #############################################3
        },
        "q4": {
            "1": {"A": ("q4", "")},
            "": {"$": ("q5", "")}
            #############################################3
        },
    },
    initial_state="q2",
    initial_stack_symbol="$",
    final_states={"q5"},
    acceptance_mode="final_state",
)

dtm3 = DTM(
    states={"q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"},
    input_symbols={"0", "1"},
    tape_symbols={"0", "1", "#", ".", "x"},
    transitions={
        #####################################################
        "q1": {"1": ("q3", "x", "R"), "0": ("q2", "x", "R"), "#": ("q8", "#", "R")},
        #####################################################
        "q2": {"0": ("q2", "0", "R"), "1": ("q2", "1", "R"), "#": ("q4", "#", "R")},
        #####################################################
        "q3": {"0": ("q3", "0", "R"), "1": ("q3", "1", "R"), "#": ("q5", "#", "R")},
        #####################################################
        "q4": {"x": ("q4", "x", "R"), "0": ("q6", "x", "L")},
        #####################################################
        "q5": {"x": ("q5", "x", "R"), "1": ("q6", "x", "L")},
        #####################################################
        "q6": {
            "0": ("q6", "0", "L"),
            "1": ("q6", "1", "L"),
            "x": ("q6", "x", "L"),
            "#": ("q7", "#", "L"),
        },
        #####################################################
        "q7": {"x": ("q1", "x", "R"), "0": ("q7", "0", "L"), "1": ("q7", "1", "L")},
        #####################################################
        "q8": {"x": ("q8", "x", "R"), ".": ("q9", ".", "R")},
        #####################################################
    },
    initial_state="q1",
    blank_symbol=".",
    final_states={"q9"},  # ,'q10'}
)
dtm4 = DTM(
    states={
        "qac",
        "q0",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "q9",
        "q10",
        "q11",
    },
    input_symbols={"0", "1", "+"},
    tape_symbols={"0", "1", "+", "C", "O", " ", "I"},
    transitions={
        "q0": {"1": ("q6", "C", "L"), "0": ("q4", "C", "L"), "+": ("q1", " ", "L")},
        #####################################################
        "q1": {
            "1": ("q1", "1", "L"),
            "0": ("q1", "0", "L"),
            "I": ("q1", "1", "L"),
            "O": ("q1", "0", "L"),
            " ": ("q10", " ", "R"),
        },
        #####################################################
        "q2": {
            "1": ("q2", "1", "R"),
            "0": ("q2", "0", "R"),
            "+": ("q2", "+", "R"),
            " ": ("q0", " ", "L"),
        },
        #####################################################
        "q3": {
            "1": ("q3", "1", "R"),
            "0": ("q3", "0", "R"),
            "O": ("q3", "O", "R"),
            "I": ("q3", "I", "R"),
            "+": ("q3", "+", "R"),
            "C": ("q0", "0", "L"),
        },
        #####################################################
        "q4": {"0": ("q4", "0", "L"), "1": ("q4", "1", "L"), "+": ("q5", "+", "L")},
        #####################################################
        "q5": {
            "1": ("q3", "I", "R"),
            "0": ("q3", "O", "R"),
            " ": ("q3", "O", "R"),
            "O": ("q5", "O", "L"),
            "I": ("q5", "I", "L"),
        },
        #####################################################
        "q6": {"0": ("q6", "0", "L"), "1": ("q6", "1", "L"), "+": ("q7", "+", "L")},
        #####################################################
        "q7": {
            "0": ("q8", "I", "R"),
            " ": ("q8", "I", "R"),
            "1": ("q9", "O", "L"),
            "O": ("q7", "O", "L"),
            "I": ("q7", "I", "L"),
        },
        #####################################################
        "q8": {
            "1": ("q8", "1", "R"),
            "0": ("q8", "0", "R"),
            "O": ("q8", "O", "R"),
            "I": ("q8", "I", "R"),
            "+": ("q8", "+", "R"),
            "C": ("q0", "1", "L"),
        },
        #####################################################
        "q9": {"1": ("q9", "0", "L"), "0": ("q8", "1", "R"), " ": ("q8", "1", "R")},
        #####################################################
        "q10": {"1": ("q10", "1", "R"), "0": ("q10", "0", "R"), " ": ("q11", " ", "R")},
        #####################################################
        "q11": {"0": ("q11", " ", "R"), "1": ("q11", " ", "R"), " ": ("qac", " ", "R")},
    },
    initial_state="q2",
    blank_symbol=" ",
    final_states={"qac"},  # ,'q10'}
)

dfa5 = DFA(
    states={'q0', 'q1', 'q2','q3','q4','q5'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q2', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q4', '1': 'q3'},
        'q3': {'0': 'q4', '1': 'q3'},
        'q4': {'0': 'q5', '1': 'q4'},
        'q5': {'0': 'q5', '1': 'q5'}, 
    },
    initial_state='q0',
    final_states={'q5'}
)

nfa6 = NFA(
    states={'q1', 'q2', 'q3','q4'},
    input_symbols={'1', '0'},
    transitions={
        'q1': {'0': {'q1'},'1':{'q1','q2'}},    # Use '' as the key name for empty string (lambda/epsilon) transitions
        'q2': {'0': {'q3'},'':{'q3'}},
        'q3': {'1': {'q4'}},
        'q4': {'0':{'q4'},'1':{'q4'}}
    },
    initial_state='q1',
    final_states={'q4'}
)

def input1(my_input_str):
    if npda1.accepts_input(my_input_str):
        print("cadena aceptada")
    else:
        print("cadena rechazada")
    print("")
    return "Gracias"


def input2(my_input_str):
    if dpda2.accepts_input(my_input_str):
        print("cadena aceptada")
    else:
        print("cadena rechazada")
    print("")
    return "Gracias"


def input3(my_input_str):
    if dtm3.accepts_input(my_input_str):
        print("cadena aceptada")
    else:
        print("cadena rechazada")
    print("")
    return "Gracias"


def input4(my_input_str):
    if dtm4.accepts_input(my_input_str):
        print("cadena aceptada")
        print("")
        x = list(dtm4.read_input(my_input_str)[1][0])
        print("La suma es : " + "".join(x))
    else:
        print(
            "cadena rechazada ingrese una cadena del tipo v+w donde v y w est??n en binario"
        )
    print("")
    return "Gracias"

def input5(my_input_str):
    if dfa5.accepts_input(my_input_str):
        print("cadena aceptada")
    else:
        print("cadena rechazada")
    print("")
    return "Gracias"

def input6(my_input_str):
    if nfa6.accepts_input(my_input_str):
        print("cadena aceptada")
    else:
        print("cadena rechazada")
    print("")
    return "Gracias"

def menu():
    
    print(100 * "-")
    print("Las m??quinas disponibles son las siguientes: ")
    print(
        "1)Automata de pila que reconoce el lenguaje en binario que tiene igual n??mero de 0s y de 1s"
    )
    print("2) Autom??ta de pila que reconoce el lenguaje binario 0^n 1^n")
    print(
        "3)M??quina de Turing determinista de una cinta que reconoce si 2 cadenas en binario son iguales(Ingrese el input como w#v)"
    )
    print(
        "4) M??quina de Turing determinista de una cinta que computa la suma de 2 cadenas binarias, ingrese v+w"
    )
    print("5) Autom??ta finito determinista que reconoce las cadenas en binario  que tienen minimo 3 0's")
    print("6) Autom??ta finito no determinista que reconoce las cadenas en binario que tengan a 11 o 101 como subcadena")
    print("#)Salir del programa ")
    x = input("Ingrese la m??quina que desea utilizar: ")
    if x == "#":
        print("")
        print("Hasta luego, gracias por utilizar el programa")
        print(100 * "-")
        return ""
    y = input("Ingrese la cadena: ")
    print("")
    if x == "1":
        print(input1(y))
        print(100 * "-")
        menu()
    elif x == "2":
        print(input2(y))
        print(100 * "-")
        menu()
    elif x == "3":
        print(input3(y))
        print(100 * "-")
        menu()
    elif x == "4":
        print(input4(y))
        print(100 * "-")
        menu()
    elif x == "5":
        print(input5(y))
        print(100*'-')
        menu()
    elif x== "6":
        print(input6(y))
        print(100*"-")
        menu()
    else:
        print("Error, ingrese un input v??lido")
        print("")
        print(100 * "-")
        menu()

menu()
