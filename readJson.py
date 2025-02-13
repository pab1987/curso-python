import json

with open('./json/products.json', mode='r') as file:
    products = json.load(file)
    
#Mostrar el json
for product in products:
    # print(product)
    print(f"Product: {product['name']} --- Price: {product['price']}")