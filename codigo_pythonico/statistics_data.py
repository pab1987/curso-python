import statistics
import csv

# Guardar el archivo CSV
''' file_path = "./files/python-CSV/sales_data.csv"
with open(file_path, "w") as file:
    file.write(csv_content)

# Devolver la ruta del archivo guardado
file_path '''

monthlySales = {}

with open('./files/python-CSV/monthly_sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        month = row['month']
        sales = float(row['sales'])
        
        monthlySales[month] = sales
        
sales = list(monthlySales.values())
#print(sales)

# Hallar ma media de los datos
meanSales = statistics.mean(sales)
print(meanSales)


# Hallar ma mediana de los datos
medianSales = statistics.median(sales)
print(medianSales)


# Hallar ma moda de los datos
modeSales = statistics.mode(sales)
print(modeSales)


#Hallar la desviación Estándar de las ventas
stdevSales = statistics.stdev(sales)
print(stdevSales)


#Hallar la varianza de las ventas
varianceSales = statistics.variance(sales)
print(varianceSales)


#Hallar la máximo de las ventas
maximo = max(sales)
print(maximo)


#Hallar la mínimo de las ventas
minimo = min(sales)
print(minimo)

#Hallar la rango de las ventas
rango = maximo - minimo
print(rango)


