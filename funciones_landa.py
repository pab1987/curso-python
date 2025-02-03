suma = lambda a, b: a + b
print(suma(10,5))


multi = lambda a, b: a * b
print(multi(10, 12))


# Cuadrado de cada número 
numbers = range(11)

numerosCuadrados = list(map(lambda x: x ** 2, numbers))
print(numerosCuadrados)

# Pares con lambda
pares = list(filter(lambda x: x % 2 == 0, numbers))
print('Números pares: ', pares)