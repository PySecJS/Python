class Person:
    # class attribute / properties
    Palinam = "male"
    
    def __init__(self, name, age): 
        # instance attribute / properties     
        self.Peyar = name
        self.Vayatu = age
    
    def gender(self):
        return "I am {} age is {} gender {}".format(self.Peyar, self.Vayatu,self.Palinam)


obj1 = Person("Raja", 18)

# access the instance attribute / properties
print(obj1.Peyar)
print(obj1.Vayatu)

# access the class attribute / properties
print(Person.Palinam)
print(obj1.gender())
print("gender {}".format(obj1.__class__.Palinam))