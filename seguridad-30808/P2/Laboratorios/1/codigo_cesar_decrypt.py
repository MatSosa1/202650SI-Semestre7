import sys


def descifrar_cesar(texto, desplazamiento=3):
    resultado = ""

    print(f"Texto cifrado: {texto}")
    print(f"Desplazamiento: {desplazamiento}")
    print("\nProceso de descifrado:")
    print("-" * 60)

    for i, caracter in enumerate(texto):
        print(f"\nCarácter {i + 1}: '{caracter}'")

        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')

            posicion_cifrada = ord(caracter) - base
            print(f"Posición cifrada: {posicion_cifrada}")

            posicion_original = (
                posicion_cifrada - desplazamiento
            ) % 26

            print(
                f"({posicion_cifrada} - {desplazamiento}) % 26 "
                f"= {posicion_original}"
            )

            caracter_original = chr(
                posicion_original + base
            )

            print(
                f"Carácter descifrado: "
                f"'{caracter_original}'"
            )

            resultado += caracter_original
        else:
            print("No es una letra, se conserva igual.")
            resultado += caracter

    print("\n" + "-" * 60)
    print(f"Mensaje original: {resultado}")

    return resultado


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Uso: python descifrar_cesar.py "
            '"mensaje_cifrado"'
        )
        sys.exit(1)

    mensaje_cifrado = " ".join(sys.argv[1:])

    descifrar_cesar(mensaje_cifrado)
