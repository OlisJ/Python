class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")


kafshe=Animal()
kafshe.sound()

rex=Dog()
rex.sound()

tom=Cat()
tom.sound()