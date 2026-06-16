import sys


def cifrar_cesar(texto, desplazamiento=5):
    resultado = ""

    print(f"Texto original: {texto}")
    print(f"Desplazamiento: {desplazamiento}")
    print("\nProceso de cifrado:")
    print("-" * 60)

    for i, caracter in enumerate(texto):
        print(f"\nCarácter {i + 1}: '{caracter}'")

        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')

            posicion_original = ord(caracter) - base
            print(f"Posición original: {posicion_original}")

            nueva_posicion = (posicion_original + desplazamiento) % 26
            print(
                f"({posicion_original} + {desplazamiento}) % 26 "
                f"= {nueva_posicion}"
            )

            nuevo_caracter = chr(nueva_posicion + base)
            print(f"Carácter cifrado: '{nuevo_caracter}'")

            resultado += nuevo_caracter
        else:
            print("No es una letra, se conserva igual.")
            resultado += caracter

    print("\n" + "-" * 60)
    print(f"Resultado final: {resultado}")

    return resultado


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python codigo_cesar.py <mensaje>")
        sys.exit(1)

    # Une todos los argumentos por si el mensaje tiene espacios
    mensaje = " ".join(sys.argv[1:])

    cifrar_cesar(mensaje)
