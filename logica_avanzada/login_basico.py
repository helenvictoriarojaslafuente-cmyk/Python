usuario = str(input('Ingrese usuario: '))
contraseña = str(input('Ingrese contraseña: '))
if (usuario == 'admin') and (contraseña == '1234'):
    print('acceso permitido')
else:
    print('acceso denegado')