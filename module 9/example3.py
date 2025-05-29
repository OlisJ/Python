class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Some generic animal sound")
    def description(self):
        print(f"this is an animal named {self.name}")

class Dog(Animal):
    def __init__(self,breed,name):
        self.breed=breed
        super().__init__(name) #ketu thirret konstruktori i superklases
    def sound(self):
        print("Woof Woof!")

    def description(self):
        super().description()
        print(f"Breed:{self.breed}")


class Cat(Animal):
    def sound(self):
        print("Meow!")
    def description(self):
        super().description()
        print(f"Color:{self.color}")
    def __init__(self,color,name):
        self.color=color
        super().__init__(name)


rex=Dog("Golden Retriever","Rex")
rex.sound()
rex.description()

Tom=Cat("Gray","Tom")
Tom.sound()
Tom.description()