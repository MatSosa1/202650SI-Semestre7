passwords = ["admin123", "qwerty"]
user_input = input("Contraseña: ")
if user_input in passwords:
    print("Acceso concedido")
else:
    print("Acceso denegado")