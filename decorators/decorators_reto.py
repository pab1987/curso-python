import functools
import datetime

# Dercorador que registra acción en el archivo
def log_employee_action(func):
    @functools.wraps(func) # Mantener el nombre original de la función
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        function_name = func.__name__

        # Guardar acción del empleado
        with open("employee_actions.log", "a") as file:
            file.write(f"{timestamp} - Acción: {function_name} - Args: {args}, Kwargs: {kwargs}\n")
        return func(*args, **kwargs) # Ejecutar función riginal
    return wrapper

# Función que representan acciones del los empleados

@log_employee_action
def realizar_tarea(nombre_empleado, tarea):
    print(f"{nombre_empleado} está realizando la tarea: {tarea}.")

@log_employee_action
def marcar_entrada(nombre_empleado):
    print(f"{nombre_empleado} ha marcado su entrada a trabajar.")

@log_employee_action
def marcar_salida(nombre_empleado):
    print(f"{nombre_empleado} ha marcado su salida de trabajar.")

# Simulación de acciones
realizar_tarea('Pablo', 'Revisar inventario')
marcar_entrada('Miguel')
marcar_salida('Juanita')