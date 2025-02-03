a = [0,1,2,3,4,5,6]

print("Lista: ", a)

print("Mayor: ", max(a))
print("Menor: ", min(a))

b = a

print(a)
print(b)

# Cuando copiamos una lista a otra, lo que se haga en una se refelja en la otra
del a[0]

print(a)
print(b)

# Para copiar solo el contenido sin  apuntar al mismo espacio en memoria se hace con el slice

c = a[:] # Se copia desde la primer posición hasta la última

print(id(a))
print(id(b))
print(id(c))