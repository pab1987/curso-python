import os

# Obtener el directorio actual
''' cwb = os.getcwd()

print('Directorio actual: ',cwb)


# Listar los archivos
txtFiles = [f for f in os.listdir('./files/') if f.endswith('.txt')]

print('Los archivos txt: ', txtFiles) '''


os.rename('cuento.txt', 'cuento.txt')

txtFiles = [f for f in os.listdir('.') if f.endswith('.txt')]

print('Los archivos txt: ', txtFiles)