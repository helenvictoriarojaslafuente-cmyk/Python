p1 = int(input("Nivel Jugador 1: "))
p2 = int(input("Nivel Jugador 2: "))
if p1 > p2:
    print("El Jugador 1 tiene el nivel más alto")
elif p2 > p1:
    print("El Jugador 2 tiene el nivel más alto")
else:
    print("Ambos niveles son iguales")