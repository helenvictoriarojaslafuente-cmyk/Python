cantidad = int(input("Cantidad de artículos: "))
if cantidad > 12:
    print("Descuento del 15%")
elif 6 <= cantidad <= 12:
    print("Descuento del 5%")
else:
    print("Sin descuento")