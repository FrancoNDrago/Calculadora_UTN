from calculadora_practica import *
from menu import *


while True:
    numero1 = int(input("Ingrese un número: "))
    numero2 = int(input("Ingrese otro número: "))    

    menu = imprimir_menu()
    respuesta = int(input(f"Los números son: A: {numero1} y B: {numero2} \nIngrese un numero del menú para realizar una operación: "))

    match respuesta:
        case 1:
            suma = suma_numeros(numero1, numero2)
            print(suma)
        case 2:
            resta = resta_numeros(numero1, numero2)
            print(resta)
        case 3:
            multiplicacion = multiplicar_numeros(numero1, numero2)
            print(multiplicacion)
        case 4:
            division = dividir_numeros(numero1, numero2)
            print(division)
        case 5:
            factoriar = factoriar_numero(numero1)
            factoriar2 = factoriar_numero2(numero2)
            print(f"Los factoriales del A son: {factoriar} \nLos factoriales del B son: {factoriar2}")
        case 0:
            break