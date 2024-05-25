def validar_respuesta(mensaje):
    while True:
        try:
            entrada = int(input(mensaje))
            return entrada
        except ValueError:
            print("Error: Ingrese un número entero válido.")