class MyClass:
    def __init__(self):
        self.__private_variable="This is mucho private"

    def __private_method(self):
        print("THis is a private method")

my_class=MyClass()
print(my_class.__private_varibale)
print(my_class.__private_method)
#show errors beacause theyre privates and cant be used outside the class