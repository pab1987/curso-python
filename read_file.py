# Leer archivo línea por línea
""" with open('caperucita.txt', 'r') as file: # Usamos open para abrir el archivo y usamos el parametro de r para leer y renombramos como file
    for lineas in file: # recorremos el archivo 
        print(lineas.strip()) #Imprimimos las lineas y quitamos los saltos de linea """
        
# Leer todas las líneas del archivo en una lista.
""" with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  """
    
# Agregar texto al archivo
""" with open('caperucita.txt', 'a') as file: # Con el atributo 'a' se hace referencia a append
    file.write("\n\nBy: Chat GPT") """
    
# Sobreescribir el texto
""" with open('caperucita.txt', 'w') as file: # Con el atributo 'w' se escribe en el archivo
    file.write("\n\nBy: Chat GPT") """
    
# Contar las lineas del archivo
with open('./files/caperucita.txt', 'r') as file: # Usamos open para abrir el archivo y usamos el parametro de r para leer y renombramos como file
    num_lineas = sum(1 for line in file)
    print(f"El numero de líneas del archivo es {num_lineas}")
    
    