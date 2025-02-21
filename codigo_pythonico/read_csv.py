import csv

# Leer archivo csv
""" with open("./files/python-CSV/products.csv", "r") as fileCsv:
    csvReader = csv.DictReader(fileCsv)
    for lineas in csvReader:
        print(lineas) """
        
        
# Mostrar la información por columnas
with open("./files/python-CSV/products.csv", "r") as fileCsv:
    csvReader = csv.DictReader(fileCsv)
    for row in csvReader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")