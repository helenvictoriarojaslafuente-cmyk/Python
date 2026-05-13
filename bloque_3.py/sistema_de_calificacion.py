nota = float(input("Ingresa la nota del estudiante: "))
if nota >= 90:
    print("Calificacion: Excelente: ")
elif nota >= 61 and nota <= 89:
    print("Calificacion: Aprobado: ")
else:
    print("Calificacion: Reprobado:")