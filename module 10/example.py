#decorators getters and setters
class Student:
    def __init__(self,name,age):  #konstruktori i classes
        self.__name=name #ketu deklarohen atributet e klases
        self.__age=age
    # deklarimi i metodes get
    @property
    def name(self):
        return self.__name
    #deklarimi i metodes set
    @name.setter
    def name(self,name):
        self.__name=name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age


student1=Student("Alice",17)
print("Name",student1.name)


student1.name="Bob"
student1.age=18

print("Name:",student1.name)