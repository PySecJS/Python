# Create a new class 
class Person:
    # Method / Function
    def __init__(self, name, age):
         # instance attribute / properties   
        self.Peyar = name
        self.Vayatu = age
    # Method / Function
    def gender(self,Palinam):
        return "I am {} age is {} gender {}".format(self.Peyar, self.Vayatu, Palinam)

    
# Object used by calling class
obj1 = Person("Raja", 18)

print(obj1.Peyar)
print(obj1.Vayatu)

# Object used by calling class
print(Person.gender(obj1,"Male"))

# Object used by calling method
print(obj1.gender("Male"))