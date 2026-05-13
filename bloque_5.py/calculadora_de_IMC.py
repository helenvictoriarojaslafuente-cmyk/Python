peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")
if imc > 25:
    print("Resultado: Sobrepeso")
else:
    print("Resultado: Peso normal o bajo")