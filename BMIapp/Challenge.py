from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    @abstractmethod
    def print_info(self):
        pass


class Adult(Person):
    def __init__(self,name,age,weight,height):
        super().__init__(name,age,weight,height)


    def calculate_bmi(self):
        bmi=self.weight/self.height
        return bmi


    def get_bmi_category(self):
        bmi=self.calculate_bmi()
        if bmi <14:
            return f"This person is Underweight"
        elif 14<bmi<18:
            return f"This person is Normal"
        elif 18<=bmi<24:
            return f"This person is Overweight"
        else:
            return f"This person is obese"

    def print_info(self):
        print(f" {self.name} Age: {self.age} Height: {self.height} Weight: {self.weight} Category:{self.get_bmi_category()}")


class Child(Person):
    def __init__(self,name,age,weight,height):
        super().__init__(name,age,weight,height)

    def calculate_bmi(self):
        bmi=(self.weight/self.height)*1.3
        return bmi


    def get_bmi_category(self):
        bmi=self.calculate_bmi()
        if bmi <14:
            return f"This person is Underweight"
        elif 14<bmi<18:
            return f"This person is Normal"
        elif 18<=bmi<24:
            return f"This person is Overweight"
        else:
            return f"This person is obese"

    def print_info(self):
        print(f" {self.name} Age: {self.age} Height: {self.height} Weight: {self.weight},Category:{self.get_bmi_category()}")


Alisa=Adult("Alissa",25,65,1.70)
print(Alisa.print_info())


Melisa=Child("Melisa",17,42,1.70)
print(Melisa.print_info())

class BMIApp:
    def __init__(self):
        people=[]

    def add_person(self):


