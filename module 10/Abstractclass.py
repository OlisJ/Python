from abc import ABC, abstractmethod


class ClassName(ABC): #this is the final definition of an abstract class ABC is important
    pass

class Shape(ABC): #klase abstrakte
    #metode abstrakte
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length*self.length

#objekte per keto 2 klas
circle_1=Circle(7)
square_1= Square(18)

print(circle_1.area())
print(square_1.area())

#klasat abstrakte mund te ket metoda te thjeshta dhe abstrakte
#interfaces jane klasa abstrakte qe kan vetem metoda abstrakte
