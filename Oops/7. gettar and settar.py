class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of")

x = Student("Mike", "Olsen")
x.welcome()
