# RSA básico en Python (solo para fines educativos)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Parámetros básicos (pequeños por simplicidad)
p = 17
q = 23
n = p * q
phi = (p-1)*(q-1)
e = 3
d = modinv(e, phi)

mensaje = 89
cifrado = pow(mensaje, e, n)
descifrado = pow(cifrado, d, n)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {cifrado}")
print(f"Mensaje descifrado: {descifrado}")