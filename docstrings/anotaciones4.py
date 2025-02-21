from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca el id del empleado en una lista de ids y retorna el id encontrado o none si no lo halla.
    """
    
    if employee_id in employee_ids:
        return employee_id
    return None  

# Llamado de la función

