class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f"Empleado: {self.name}")
        print(f"skills: {self.skills}")
        print(f"details: {self.details}")

employee = Employee('Carlos', 'Python', 'Java', 'C#', age=37, city='Bogota')
employee.show_employee()