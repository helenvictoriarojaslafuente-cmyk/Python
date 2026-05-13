password = input("Ingresa una nueva contraseña: ")
longitud_minima = 10
if len(password) >= longitud_minima:
    print("Contraseña válida.")
else:
    faltantes = longitud_minima - len(password)
    print(f"Contraseña demasiado corta. Te faltan {faltantes} caracteres.")