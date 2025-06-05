class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name= name


    def get_age(self):
        return self.__age
    def set_age(self, name):
         self.__age=age


Student1=Student("Olti","18")
print("name:",Student1.get_name())
Student1.set_name("Usame")
print("Updated Name:",Student1.get_name())
