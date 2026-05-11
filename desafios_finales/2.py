nota = int(input('Introduce tu nota: '))

if 90 <= nota <= 100:
    clasificacion = 'A'
elif 80 <= nota <= 90:
    clasificacion = 'B'
elif 70 <= nota <= 80:
    clasificacion = 'C'
elif 60 <= nota <= 70:
    clasificacion = 'D'
elif 0 <= nota <= 60:
    clasificacion = 'F'
else:
    clasificacion = 'Nota invalida'

print('Su nota es: ', nota, ' y su calificacion es ', clasificacion)