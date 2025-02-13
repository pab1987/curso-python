class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        return f"{self.name} dice: Hola."
    
class Worker:
    def __init__(self, job):
        self.job = job
        
    def work(self):
        return f"Trabajando como {self.job}."

# Herencia multiple

class Emploee(Person, Worker):
    # Llamar a los constructores de las clases base
    def __init__(self, name, age, job, salary):
        super().__init__(name, age)
        Worker.__init__(self, job)
        self.salary = salary
        
    def details(self):
        return f"{self.name}, {self.age} años, trabaja como {self.job} y gana {self.salary}."
    
# Instancia de las clases
employee = Emploee('pablo', 37, 'Software Developer', 5250000)
print(employee.speak())
print(employee.work())
print(employee.details())
