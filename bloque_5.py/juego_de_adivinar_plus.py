numero_secreto = 42
intento = 0
while intento != numero_secreto:
    intento = int(input("Adivina el número secreto: "))
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else: 
        print("¡Felicidades! Adivinaste el número.")