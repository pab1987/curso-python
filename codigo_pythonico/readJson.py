import json

with open('./json/products.json', mode='r') as file:
    products = json.load(file)
    
#Mostrar el json
''' for product in products:
    # print(product)
    print(f"Product: {product['name']} --- Price: {product['price']}")
     '''

newProduct = {
    'name': 'Wireless Chager',
    'price': '75',
    'quantity': 100,
    'brand': 'ChartgerMaster',
    'category': 'Accessories',
    'entry_date': '2025-02-12'
}
    
products.append(newProduct)

with open('./json/products.json', 'w') as file:
    json.dump(products, file, indent=4)