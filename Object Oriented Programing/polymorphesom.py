class Square():
    def __init__(self, side):
        self.side=side
    __name="Anha"
    def area(self):
        print("The total are of this platform is:",self.side**2)
        print(self.__name)
    
    def __area2(self):
        print("The total are of this platform is:",self.side**2)

class Circle():
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        print("The total ratio of this platform is:", 3.1416*self.radius**2)
ob_of_square=Square(2)
ob_of_circle=Circle(5)
for shape in(ob_of_square, ob_of_circle):
    shape.area()
