# Create a new class 
class Person:
# Method / Function
    def __init__(self, name, age):
        # instance attribute / properties   
        self.Peyar = name
        self.Vayatu = age
    def __repr__(self):
         return "I am {} age is {} gender".format(self.Peyar, self.Vayatu)

# Object used by calling class
obj1 = Person("Raja", 18)

print(obj1)
