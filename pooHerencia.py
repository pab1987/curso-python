class Vehiculo:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.isAvailable = True
        
    # Método para vender los vehículos
    def sell(self):
        if self.isAvailable:
            self.isAvailable = False
            print(f"El vehiculo {self.brand} {self.model}, ha sido vendido.")
        else:
            print(f"El vehiculo {self.brand}, no está disponible.")
            
    # Método para ver la disponibilidad de los vehículos
    def checkAvailable(self):
        return self.isAvailable
    
    # Método para verificar el precio de los vehículos
    def getPrice(self):
        return self.price
    
    # Iniciar motor del vehículo
    def startEngine(self):
        raise NotImplementedError('Este método debe ser implementado por la subclase')
    
    # Detener motor del vehículo
    def stopEngine(self):
        raise NotImplementedError('Este método debe ser implementado por la subclase')
    
## Clase que hereda de la clase padre. Se le pasa la clase padre como si fuera un argumento.
class Car(Vehiculo):
    
    def startEngine(self):
        if not self.isAvailable:
            return f"El motor del vehículo {self.brand}, está en marcha"
        else:
            f"El motor del vehículo {self.brand}, está detenido"
            
    def stopEngine(self):
        if self.isAvailable:
            return f"El motor del vehículo {self.brand}, se ha detenido"
        else:
            return f"El motor del vehículo {self.brand}, no está disponible"
        
        
class Bike(Vehiculo):
    
    def startEngine(self):
        if not self.isAvailable:
            return f"La bicicleta {self.brand}, está en marcha"
        else:
            f"La bicicleta {self.brand}, está detenido"
            
    def stopEngine(self):
        if self.isAvailable:
            return f"La bicicleta {self.brand}, se ha detenido"
        else:
            return f"La bicicleta {self.brand}, no está disponible"
        
class Truck(Vehiculo):
    
    def startEngine(self):
        if not self.isAvailable:
            return f"El camión {self.brand}, está en marcha"
        else:
            f"El camión {self.brand}, está detenido"
            
    def stopEngine(self):
        if self.isAvailable:
            return f"El camión {self.brand}, se ha detenido"
        else:
            return f"El camión {self.brand}, no está disponible"

class Customer:
    
    def __init__(self, name):
        self.name = name
        self.pusrchasedVehicles = []
    
    def buyVehicle(self, vehicle: Vehiculo):
        if vehicle.checkAvailable():
            vehicle.sell()
            self.pusrchasedVehicles.append(vehicle)
        else:
            print(f"Sorry, {vehicle.brand} isn't available.")
            
    def inquireVehicle(self, vehicle: Vehiculo):
        if vehicle.checkAvailable():
           availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El vehiculo {vehicle.brand} se encuentra {availablity} y cuesta {vehicle.getPrice()}") 

class DealerDhip:
    def __init__(self):
        self.inventory = []
        self.customers = []
        
    def addVehicles(self, vehicle: Vehiculo):
        self.inventory.append(vehicle)
        print(f"El vehículo {vehicle.brand} {vehicle.model} ha sido añadido al inventario")
    
    def registerCustomers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido al listado de clientes")
        
    def showAvailableVehicles(self):
        print("Vehiculos disponibles en el consesionario")
        for vehicle in self.inventory:
            if vehicle.checkAvailable():
                print(f"- {vehicle.brand} {vehicle.model} por {vehicle.getPrice()}")
                
                
car = Car("Toyota", "Prado TXL", 300000000)
car2 = Car("Toyota", "Fortuner", 200000000)
bike = Bike("GW", "Cross", 1500000)
truck = Truck("Kodia", "Diesel 5000", 650000000)


customer = Customer("Pablo")

dealerShip = DealerDhip()

dealerShip.addVehicles(car)
dealerShip.addVehicles(car2)
dealerShip.addVehicles(bike)
dealerShip.addVehicles(truck)

# Mostrar vehículos disponibles
dealerShip.showAvailableVehicles()

#Cliente consulta un vehículo
customer.inquireVehicle(car)

# Cliente compra vehículo
customer.buyVehicle(car)

# Mostrar vehículos disponibles
dealerShip.showAvailableVehicles()


        
    