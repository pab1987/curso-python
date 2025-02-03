


# Métodos de Diccionarios en Python

# Diccionario de ejemplo
datos = {"nombre": "Pablo", "edad": 37, "hobbie": "Estudiar"}

# Acceso y consulta
print(datos.get("nombre"))  # 'Pablo': Obtener el valor de una clave
print(datos.get("altura", "No definida"))  # 'No definida': Valor predeterminado
print(datos.keys())  # dict_keys(['nombre', 'edad', 'hobbie']): Todas las claves
print(datos.values())  # dict_values(['Pablo', 37, 'Estudiar']): Todos los valores
print(datos.items())  # dict_items([('nombre', 'Pablo'), ('edad', 37), ('hobbie', 'Estudiar')]): Claves y valores

# Adición y actualización
datos.update({"altura": 1.73})  # Agrega o actualiza claves y valores
print(datos)  # {'nombre': 'Pablo', 'edad': 37, 'hobbie': 'Estudiar', 'altura': 1.73}
datos.setdefault("peso", 75)  # Agrega 'peso' si no existe; no modifica si ya está
print(datos)  # {'nombre': 'Pablo', 'edad': 37, 'hobbie': 'Estudiar', 'altura': 1.73, 'peso': 75}

# Eliminación
print(datos.pop("edad"))  # 37: Elimina y devuelve el valor de la clave 'edad'
print(datos.pop("genero", "No especificado"))  # 'No especificado': Valor predeterminado si la clave no existe
print(datos.popitem())  # ('peso', 75): Elimina y devuelve el último par clave-valor
datos.clear()  # Vacía el diccionario
print(datos)  # {}

# Creación de un nuevo diccionario para demostración adicional
datos = {"nombre": "Pablo", "edad": 37, "hobbie": "Estudiar"}

# Copia y comparación
nuevo_datos = datos.copy()  # Crea una copia del diccionario
print(nuevo_datos == datos)  # True: Verifica si son iguales
print(nuevo_datos is datos)  # False: Verifica si son el mismo objeto en memoria
