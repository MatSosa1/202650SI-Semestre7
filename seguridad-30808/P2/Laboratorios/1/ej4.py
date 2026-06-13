def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')

            nuevo_caracter = chr(
                (ord(caracter) - base + desplazamiento) % 26 + base
            )

            resultado += nuevo_caracter
        else:
            # Mantener espacios, números y símbolos
            resultado += caracter

    return resultado


def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)


def obtener_desplazamiento():
    while True:
        try:
            valor = int(input("Ingrese el desplazamiento (entero): "))
            return valor
        except ValueError:
            print("Error: debe ingresar un número entero.")


def pruebas():
    print("\n=== PRUEBAS AUTOMÁTICAS ===")

    mensaje = "Hola Mundo"
    clave = 3

    cifrado = cifrado_cesar(mensaje, clave)
    descifrado = descifrado_cesar(cifrado, clave)

    print(f"Mensaje original : {mensaje}")
    print(f"Cifrado          : {cifrado}")
    print(f"Descifrado       : {descifrado}")

    assert descifrado == mensaje

    # Prueba de mayúsculas y minúsculas
    assert cifrado_cesar("ABC xyz", 2) == "CDE zab"

    # Prueba de caracteres especiales
    assert cifrado_cesar("Hola, Mundo! 123", 5) == "Mtqf, Rzsit! 123"

    print("Todas las pruebas fueron superadas.\n")


def menu():
    while True:
        print("\n===== CIFRADO CÉSAR =====")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Ejecutar pruebas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mensaje = input("Ingrese el mensaje: ")
            clave = obtener_desplazamiento()

            resultado = cifrado_cesar(mensaje, clave)
            print("Mensaje cifrado:", resultado)

        elif opcion == "2":
            mensaje = input("Ingrese el mensaje cifrado: ")
            clave = obtener_desplazamiento()

            resultado = descifrado_cesar(mensaje, clave)
            print("Mensaje descifrado:", resultado)

        elif opcion == "3":
            pruebas()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()