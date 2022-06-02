# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:34:45 2022

@author: Asus
"""

from automata.pda.dpda import DPDA
from automata.pda.npda import NPDA

npda1 = NPDA(
    states={"qloop", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "qfinal"},
    input_symbols={"0", "1"},
    stack_symbols={"S", "A", "B", "0", "1", "$"},
    transitions={
        "q1": {
            "": {},
        },
        "q2": {
            "": {"A": {("qloop", ("1", "A"))}},
        },
        "q3": {
            "": {"B": {("qloop", ("0", "B"))}},
        },
        "q4": {
            "": {"S": {("qloop", ("0", "S"))}},
        },
        "q5": {
            "": {"S": {("qloop", ("1", "S"))}},
        },
        "q6": {
            "": {"A": {("q7", ("A", "A"))}},
        },
        "q7": {
            "": {"A": {("qloop", ("1", "A"))}},
        },
        "q8": {
            "": {"B": {("q9", ("B", "B"))}},
        },
        "q9": {
            "": {"B": {("qloop", ("0", "B"))}},
        },
        "qloop": {
            "": {
                "S": {
                    ("q2", "A"),
                    ("q3", "B"),
                },
                "A": {
                    ("qloop", "0"),
                    ("q4", "S"),
                    ("q6", "A"),
                },
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
                },
            },
            "1": {
                "1": {
                    ("qloop", ""),
                },
            },
        },
    },
    initial_state="q1",
    initial_stack_symbol="$",
    final_states={"qfinal"},
)

dpda2 = DPDA(
    states={"q2", "q3", "q4", "q5"},
    input_symbols={"0", "1"},
    stack_symbols={"A", "B", "$"},
    transitions={
        "q2": {"0": {"$": ("q3", ("A", "$"))}},
        "q3": {"0": {"A": ("q3", ("A", "A"))}, "1": {"A": ("q4", "")}},
        "q4": {"1": {"A": ("q4", "")}, "": {"$": ("q5", "")}},
    },
    initial_state="q2",
    initial_stack_symbol="$",
    final_states={"q5"},
    acceptance_mode="final_state",
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


def menu():
    print("Las máquinas disponibles son las siguientes: ")
    print(
        "1) Automata de pila que reconoce el lenguaje en binario que tiene igual número de 0s y de 1s"
    )
    print("2) Automáta de pila que reconoce el lenguaje binario 0^n 1^n")
    x = input("Ingrese la máquina que desea utilizar: ")
    y = input("Ingrese la cadena: ")
    print("")
    if x == "#":
        print("Gracias por utilizar el programa")
    if x == "1":
        print(input1(y))
        menu()
    if x == "2":
        print(input2(y))
        menu()


menu()
