## Reto de Poo con sala de ventas de autos
class Auto:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.isAvailable = True
        
    def sell(self):
        if self.isAvailable:
            self.isAvailable = False
            print(f'El vehiculo {self.brand} {self.model} ha sido vendido ')
        else:
            print(f'El vehiculo {self.brand} {self.model} no está disponible')
            
    def checkAvailability(self):
        return self.isAvailable
    
    def getPrice(self):
        return self.price
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.carsPurchased = []
        
    def buyCar(self, car):
        if car.checkAvailability():
            car.sell()
            self.carsPurchased.append(car)
        else:
            print(f'El vehiculo {car.brand} {car.model} no está disponible')
    
    def inquireCar(self, car):
        availability = "disponible" if car.checkAvailability() else "no disponible"
        print(f"El vehiculo {car.brand} {car.model} está {availability}")
        
class Dealership:
    
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def addCar(self, car):
        self.inventory.append(car)
        print(f'El vehiculo {car.brand} {car.model} ha sido agregado al inventario')
        
    def registerCustomer(self, customer):
        self.customers.append(customer)
        print(f'El cliente {customer.name} ha sido registrado en el concesionario.')
        
    def showAvailableCars(self):
        print('Autos disponibles en el concesionario: ')
        for car in self.inventory:
            if car.checkAvailability():
                print(f"- {car.brand} {car.model} por {car.getPrice()}")
# Crear instancias de autos
car1 = Auto('Toyota', 'Prado TXL', 350000000)
car2 = Auto('Toyota', '4RUNNER', 320000000)
car3 = Auto('Toyota', 'FORTUNER', 280000000)

#Crear instancia de cliente
customer1 = Customer('Pablo')

#Crear instancia de concesionaria
dealership = Dealership()
dealership.addCar(car1)
dealership.addCar(car2)
dealership.addCar(car3)


# Mostrar coches disponibles
dealership.showAvailableCars()

#Cliente consulta coche
customer1.inquireCar(car1)

# Cliente compra coche
customer1.buyCar(car1)

# Mostrar coches disponibles
dealership.showAvailableCars()

# Cliente intenta comprar coche vendido
customer1.buyCar(car1)