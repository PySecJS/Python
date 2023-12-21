# Create a new class 
class Person:
# Method / Function
    def __init__(self, name, age):
        # instance attribute / properties   
        self.Peyar = name
        self.Vayatu = age

# Object used by calling class
obj1 = Person("Raja", 18)

# Modify object properties/attribute
obj1.Peyar="Durai"
print(obj1.Peyar)

# Delete object
del obj1.Vayatu
print(obj1.Vayatu)

# Delete class
del obj1
print(obj1)
