def suma_numeros(num1, num2):
    suma = num1 + num2

    return suma


def resta_numeros(num1, num2):
    resta = num1 - num2

    return resta


def multiplicar_numeros(num1, num2):
    multiplicacion = num1 * num2

    return multiplicacion


def dividir_numeros(num1, num2):
    while num2 <= 0:
        num2 = int(input("Ingrese un denominador mayor a 0: "))
    return num1 // num2   


def factoriar_numero(num1):
    while num1 < 0:
        num1 = int(input("Ingrese un numero positivo: "))
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num1 + 1):
            resultado *= i
        return resultado
    
def factoriar_numero2(num1):
    while num1 < 0:
        num1 = int(input("Ingrese un numero positivo: "))
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num1 + 1):
            resultado *= i
        return resultado    