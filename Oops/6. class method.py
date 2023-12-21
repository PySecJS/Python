from datetime import date 

# Create a new class 
class Person:
    # Method / Function
    def __init__(self, name, age):
         # instance attribute / properties   
        self.Peyar = name
        self.Vayatu = age

    @classmethod
    def Birthyear(cls, name2, Pirantavarutam):
        return cls(name2, date.today().year - Pirantavarutam)

    def replace(self):
        print("I am " + self.Peyar + " age is " + str(self.Vayatu))
    
# Object used by calling class
obj1 = Person("Raja", 21)
obj1.replace()

# Object used by calling classmethod
obj2 = Person.Birthyear("Durai",2001)
obj2.replace()

