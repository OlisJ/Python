class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def human_name(self):
        return self.name
    def human_age(self):
        return self.age
    def huamn_greet(self):
        print(f"Hello ,im {self.name}")

person1=human('olis',18,)
person2=human("alban",17)

person2.huamn_greet()
person1.huamn_greet()
