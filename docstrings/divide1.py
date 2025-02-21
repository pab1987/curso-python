def divide(a: int, b: int) -> float:
    '''Validar los parámetros con isinstance '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser números enteros o flotantes.')
    if b == 0:
        raise ValueError('El divisor no puede ser cero')
    return a/b

#print(divide(2,'1'))

#Ejemplo de uso de try:
try: 
    res = divide(10, 0)
    print(res)
except ValueError as e:
    print(f"Error: {e}")
