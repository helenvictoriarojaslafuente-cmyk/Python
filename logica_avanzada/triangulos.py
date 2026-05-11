lado1 = float(input('ingrese lado 1 '))
lado2 = float(input('ingrese lado 2 '))
lado3 = float(input('ingrese lado 3 '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('si, los lados', lado1, lado2, lado3, 'si pueden formar un triangulo')
else:
    print('no, los lados no forman un triangulo')
    