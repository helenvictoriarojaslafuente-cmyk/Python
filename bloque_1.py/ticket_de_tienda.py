articulo = input("nombre del articulo: ")
precio= int(input("precisio unitario: "))
cantidad= float(input("cantidad comprada: "))
total = precio * cantidad
print(f"usted compro {cantidad} unidades de {articulo}. total a pagar: {total}")