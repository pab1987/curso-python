class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")
        
        
class Student(Person):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId
        
    def greet(self):
        super().greet()
        print(f"Hello, my student id is {self.studentId}")
     
        
person = Student('Pablo', 37, 1)

person.greet()
        