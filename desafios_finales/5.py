
numero_secreto = 7


print("¡Juego de Adivinar el Número!")
print("Tengo un número secreto entre 1 y 10.")

intento = int(input("¿Cuál crees que es?: "))


if intento == numero_secreto:
    print("¡Felicidades! 🎉 Adivinaste el número.")
elif intento < numero_secreto:
    print("Muy bajo. El número secreto es mayor.")
else:
    print("Muy alto. El número secreto es menor.")

print("Fin del juego") 