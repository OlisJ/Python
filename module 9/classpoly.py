class Dog:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} Makes the sound:Ham")


class Cat:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} Makes the sound:Miau")


class Bird:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} Makes the sound:CiuCiu")


qeni=Dog("Bubi")
macja=Cat("Meows")
zogi=Bird("Ismet")


for animal in (qeni,macja,zogi):
    print(animal.sound())