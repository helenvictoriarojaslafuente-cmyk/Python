compra = int(input('ingrese el costo de su compra: '))
if compra > 100:
    total = compra * 0.90
else:
    total = compra

print('el total a pagar es ', total)