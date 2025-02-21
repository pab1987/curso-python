import csv

newProduct = {
    'name': 'Wireless Chager',
    'price': '75',
    'quantity': 100,
    'brand': 'ChartgerMaster',
    'category': 'Accessories',
    'entry_date': '2025-02-12'
}

with open('./files/python-CSV/products.csv', 'a', newline='') as file:
    # file.write('\n')
    csvWriter = csv.DictWriter(file, fieldnames= newProduct.keys())
    csvWriter.writerow(newProduct)
    print(csvWriter)