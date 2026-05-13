saldo = float(input("¿Cuánto dinero tiene en su cuenta?: "))
retiro = float(input("¿Cuánto desea retirar?: "))
if saldo >= retiro:
    print(f"Operación exitosa. Saldo restante: {saldo - retiro}")
else: 
    print("No se puede realizar la operación: Saldo insuficiente.")