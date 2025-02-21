""" numbers = []
pares = []
impares = []

limit = 1

while limit <= 100:
    numbers.append(limit)
    if limit % 2 == 0:
        pares.append(limit)
    else:
        impares.append(limit)
    limit += 1
    
print('Números pares: ', pares)
print('Números impares: ', impares) """

print('======================================')

def generador_numeros():
    limit = 1
    while limit <= 100:
        yield limit
        limit += 1


numeros = generador_numeros()

pares, impares = [], []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
 
print('Números pares: ', pares)
print('Números impares: ', impares)   






