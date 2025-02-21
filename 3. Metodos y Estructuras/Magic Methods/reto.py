class Employee:
    def __init__(self):
        self.employees = {}

    def add_emloyee(self, emp_id, name):
        if emp_id not in self.employees:
            self.employees[emp_id] = name
            print(f'El empleado {name}, ha sido .')
        else:
            print(f'El empleado {name}, ya fue agregado anteriormente.')
    
    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            print(f'El empleado con id: {emp_id}, no se encuentra vinculado')
        else:
            name = self.employees[emp_id]
            self.employees.pop(emp_id)
            print(f'El empleado {name}, ha sido eliminado exitosamente. ')

    def show_employee(self):
        if self.employees:
            print('Lista de empleados')
            for emp_id, name in self.employees.items():
                print(f"- ID: {emp_id}, Nombre: {name}")
    
if __name__ == '__main__':
    manager = Employee()
    manager.add_emloyee(1, 'Pablo')
    manager.add_emloyee(2, 'Miguel')
    manager.show_employee()
    manager.delete_employee(1)
    manager.show_employee()
