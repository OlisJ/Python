import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Paralelo(Shape):
    def __init__(self, width,ha):
        self.width=width
        self.ha=ha

    def area(self):
        return self.width*self.ha


paralelogrami=Paralelo(5,4)
print(paralelogrami.area())





