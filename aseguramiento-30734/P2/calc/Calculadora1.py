# calculadora.py

def sumar(a, b):
    resultado = a + b
    print("Resultado:", resultado)
    return resultado


def restar(a, b):
    resultado = a - b
    print("Resultado:", resultado)
    return resultado


def multiplicar(a, b):
    resultado = a * b
    print("Resultado:", resultado)
    return resultado


def dividir(a, b):
    if b == 0:
        print("Error: División por cero")
        return None

    resultado = a / b
    print("Resultado:", resultado)
    return resultado



def suma_avanzada(a, b):
    resultado = a + b
    print("Resultado:", resultado)
    return resultado


def resta_avanzada(a, b):
    resultado = a - b
    print("Resultado:", resultado)
    return resultado


def multiplicacion_avanzada(a, b):
    resultado = a * b
    print("Resultado:", resultado)
    return resultado


def division_avanzada(a, b):
    if b == 0:
        print("Error: División por cero")
        return None

    resultado = a / b
    print("Resultado:", resultado)
    return resultado


# --------- MENÚ ---------

while True:

    print("\nCALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n1 = float(input("Ingrese número 1: "))
        n2 = float(input("Ingrese número 2: "))
        sumar(n1, n2)

    elif opcion == "2":
        n1 = float(input("Ingrese número 1: "))
        n2 = float(input("Ingrese número 2: "))
        restar(n1, n2)

    elif opcion == "3":
        n1 = float(input("Ingrese número 1: "))
        n2 = float(input("Ingrese número 2: "))
        multiplicar(n1, n2)

    elif opcion == "4":
        n1 = float(input("Ingrese número 1: "))
        n2 = float(input("Ingrese número 2: "))
        dividir(n1, n2)

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")