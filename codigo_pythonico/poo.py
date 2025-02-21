class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")
        
person = Person('Pablo', 37)
person2 = Person('Ana', 25)

person.greet()