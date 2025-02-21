def check_access(func):
    def wrapper(employee):
        # Comprobar el rol del administrador
        if employee.get('rol') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper

@check_access
def delete_employees(employee):
    print(f'El empleado {employee['name']} ha sido eliminado.')

admin = {'name': 'Carlos', 'rol': 'admin'}
employee = {'name': 'Juan', 'rol': 'employee'}


#delete_employees(admin)
delete_employees(employee)