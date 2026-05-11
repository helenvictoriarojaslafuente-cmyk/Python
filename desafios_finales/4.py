password = input('Introduce tu contrasena para validar: ')
if len(password) > 7:
    print('Acceso concedido: La contrasena es segura.')
else:
    print('Error: La contrasena debe tener mas de 8 caracteres')
