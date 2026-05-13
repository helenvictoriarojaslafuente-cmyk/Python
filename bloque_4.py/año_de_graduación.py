actual = float(input("Ingrese el año actual: "))
graduacion = float(input("Ingrese el año de graduación: "))
diferencia = graduacion - actual
if diferencia == 1:
    print("!Casi terminas!")
elif diferencia > 1:
    print(f"Faltan {diferencia} años para graduarte")