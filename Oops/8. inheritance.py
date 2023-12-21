class Square:

    def __init__(self, width, height):
        self.Akalam = width
        self.Uyaram = height
    def square(self):
        return self.Akalam * self.Uyaram

class Rectangle(Square):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    def rectangle(self):
        return self.Akalam * self.Uyaram  

class Cube(Rectangle):
    def cube(self, lenght):
        self.Nilam = lenght
        return self.Akalam * self.Uyaram *self.Nilam      

# Object used by calling funtion
obj1 = Square(2, 2)
print(obj1.square())

obj2 = Rectangle(2, 3)
print(obj2.rectangle())

obj3 = Cube(1, 3)
print(obj3.cube(5))





