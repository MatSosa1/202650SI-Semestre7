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
            resultado += caracter
    return resultado

mensaje = input("Ingrese el mensaje: ")
clave = int(input("Ingrese el desplazamiento: "))

texto_cifrado = cifrado_cesar(mensaje, clave)
print("Texto cifrado:", texto_cifrado)
