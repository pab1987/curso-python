import csv

filePath = './files/python-CSV/products.csv'
updatedFile = 'productsUpdated.csv'

with open('./files/python-CSV/products.csv', 'r') as file:
    csvReader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldName = csvReader.fieldnames + ['total_value']
    
    with open('productsUpdated.csv', 'w', newline='') as updatedFile:
        csvWriter = csv.DictWriter(updatedFile, fieldnames=fieldName)
        csvWriter.writeheader() # Escribir encabezado
        
        for row in csvReader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csvWriter.writerow(row)