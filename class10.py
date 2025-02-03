
# 1. Agregar elementos
lista = [1, 2, 3]

# Agregar un elemento al final
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# Agregar varios elementos de un iterable
lista.extend([5, 6])
print(lista)  # [1, 2, 3, 4, 5, 6]

# Insertar un elemento en una posición específica
lista.insert(2, 'a')  # En el índice 2
print(lista)  # [1, 2, 'a', 3, 4, 5, 6]

# 2. Eliminar elementos
# Eliminar la primera aparición de un elemento
lista.remove('a')
print(lista)  # [1, 2, 3, 4, 5, 6]

# Eliminar y devolver el último elemento (o por índice)
eliminado = lista.pop()  # Sin índice elimina el último
print(eliminado)  # 6
print(lista)  # [1, 2, 3, 4, 5]

# Limpiar toda la lista
lista.clear()
print(lista)  # []

# 3. Consultar o modificar
lista = [3, 1, 2, 2, 4]

# Obtener el índice de un elemento
print(lista.index(2))  # 2 (índice de la primera aparición)

# Contar las veces que aparece un elemento
print(lista.count(2))  # 2

# Ordenar los elementos
lista.sort()
print(lista)  # [1, 2, 2, 3, 4]

# Ordenar en orden inverso
lista.sort(reverse=True)
print(lista)  # [4, 3, 2, 2, 1]

# Invertir el orden actual
lista.reverse()
print(lista)  # [1, 2, 2, 3, 4]

# 4. Copiar una lista
lista_copia = lista.copy()
print(lista_copia)  # [1, 2, 2, 3, 4]

# 5. Otros usos comunes
# Obtener la longitud de una lista
print(len(lista))  # 5

# Convertir un iterable a lista
tupla = (7, 8, 9)
lista_tupla = list(tupla)
print(lista_tupla)  # [7, 8, 9]

