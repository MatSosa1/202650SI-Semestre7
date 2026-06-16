import sys


def xor_encrypt(message, key):
    print(f"\nMensaje : {message}")
    print(f"Clave   : {key}\n")

    print(
        f"{'Caracter':<10}"
        f"{'ASCII':<10}"
        f"{'Operación XOR':<25}"
        f"{'Resultado':<15}"
    )
    print("-" * 60)

    encrypted = []

    for i, char in enumerate(message):
        key_char = [23]

        ascii_char = ord(char)
        ascii_key = ord(key_char)

        xor_result = ascii_char ^ ascii_key

        encrypted.append(chr(xor_result))

        print(
            f"{char:<10}"
            f"{ascii_char:<10}"
            f"{ascii_char} ^ {ascii_key:<15}"
            f"{xor_result:<15}"
        )

    print("-" * 60)

    print("\nTexto cifrado (valores decimales):")
    print(" ".join(str(ord(c)) for c in encrypted))

    print("\nTexto cifrado (hexadecimal):")
    print(" ".join(f"{ord(c):02X}" for c in encrypted))

    return "".join(encrypted)


def main():
    if len(sys.argv) != 3:
        print("Uso: python xor.py \"MENSAJE\" \"CLAVE\"")
        sys.exit(1)

    message = sys.argv[1]
    key = sys.argv[2]

    xor_encrypt(message, key)


if __name__ == "__main__":
    main()
