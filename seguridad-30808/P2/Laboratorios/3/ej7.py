from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generación de clave AES-256 (32 bytes = 256 bits)
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# Nonce (vector de inicialización)
nonce = os.urandom(12)

# Mensaje original
mensaje = "Seguridad informática con AES-256"
datos = mensaje.encode("utf-8")

# CIFRADO
ciphertext = aesgcm.encrypt(nonce, datos, None)

ciphertext = bytearray(ciphertext)
ciphertext[0] ^= 1
ciphertext = bytes(ciphertext)

print("MENSAJE ORIGINAL:", mensaje)
print("CLAVE:", key.hex())
print("NONCE:", nonce.hex())
print("CIFRADO:", ciphertext.hex())

# DESCIFRADO
texto_descifrado = aesgcm.decrypt(nonce, ciphertext, None)
print("DESCIFRADO:", texto_descifrado.decode("utf-8"))