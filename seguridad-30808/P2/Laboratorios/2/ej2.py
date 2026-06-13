import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

passwd = input("Introduce una contraseña: ")
print("Hash SHA-256:", hash_password(passwd))