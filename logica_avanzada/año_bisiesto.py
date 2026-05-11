año = int(input('introduce un año: '))
if (año % 400 == 0):
    print('es bisiesto')
elif (año % 100 == 0):
    print('no es bisiesto')
elif (año % 4 == 0):
    print('es bisiesto')
else:
    print('no es bisiesto')

