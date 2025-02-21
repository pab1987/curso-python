class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    def introduce(self) -> str:
        return f"Hello, my name is {self.name}, I'm {self.age} years old, and my salary is {self.salary}."
    
employee = Employee('pablo', 37, 2500)
print(employee.introduce())