""" # Ejemplo de iterador

#Lista

myList = [1,2,3,4]

#Obtener iterador
myIter = iter(myList)

#Usar el iterador
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter)) """

""" texto = "Hello world"

iterador = iter(texto)

for i in iterador:
    print('Valor de i: ', i)
    
print('==========================') """

#Iterar números impares
""" limit = 100

#Iterador
iterador = iter(range(0, limit + 1, 2))

for i in iterador:
    print('Valor del iterador: ', i) """
    
# Generador yield

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    
for generador in myGenerator():
    print(generador)