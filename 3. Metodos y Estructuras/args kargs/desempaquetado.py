""" #Desempaquetado args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print(add(*values)) 

def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
show_info(**data) """

# Desempaquetado de args
def add(a,b,c):
    return a+b+c

values = (1,2,3)
print(add(*values)) # para pasar varios parámetros como args usamos * al inicio de la variable.


def show_info(name, age):
    print(f"name: {name}, Age: {age}")

data = {"name": "Ana", "age": "40"}

show_info(**data) # para pasar una lista como parametro con varios valores ponemos ** para uso de kwargs