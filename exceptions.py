try:
    divisor = int(input('Ingresa el divisor: '))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as error:
    print('Ha ocurrido un error de tipo: ',error)
except ValueError as error:
    print('Error: Debes introducir un número válido')
    print('Error: ',error)