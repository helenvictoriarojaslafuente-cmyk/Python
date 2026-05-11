peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros (ej.1.75): '))
imc = peso / (altura ** 2)
print('Su imc es: ', imc)

if imc < 18.5:
    print('Categoria bajo de peso')
elif 18.5 <= imc < 24.9:
    print('Categoria peso normal')
elif 25 <= imc < 29.9:
    print('Categoria: sobrepeso')
else:
    print('Categoria: obesidad')