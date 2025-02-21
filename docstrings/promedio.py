def calculate_average(numbers):
    """
    Calcula el promedio de una lista de numeros.
    
    Parámetros:
    numbers (list): Puede ser números enteros o flotantes.
    
    Retorna:
    float: Promedio de números en la lista
    """
    return sum(numbers) / len(numbers)

# Imprimiendo el resultado de la función
print(calculate_average([1,2.3,4,5]))