año_de_nacimiento = int(input('Ingrese año de nacimiento '))
from datetime import date
año_actual = date.today().year
edad = año_actual - año_de_nacimiento
print('Tienes ', edad, 'a la fecha de hoy que es ', año_actual)