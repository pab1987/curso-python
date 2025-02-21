import functools
import datetime

# Decorador que comprueba el rol
def check_access(required_rol):
    def decorator(func):
        def wrapper(*args):
            #Si el rol del empleado coincide con el rol requerido
            rol = args[0]
            if isinstance(rol, dict) and rol.get('rol') == required_rol:
                return func(*args)
            else:
                print(f'ACCESO DENEGADO. Solo los {required_rol} pueden realizar esta acción')
        return wrapper
    return decorator



def log_action(func):
    @functools.wraps(func)
    def wrapper(*args):
       
       fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       function_name = func.__name__
       with open('actions.log', 'a') as file:
           file.write(f"{fecha_hora} - Action: {function_name} - Args: {args}.")
       return func(*args)
    return wrapper 

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

# Llamar a la función de acción
admin = {'name': 'Carlos', 'rol': 'admin'}
employee = {'name': 'Juan', 'rol': 'employee'}

delete_employee(employee)



