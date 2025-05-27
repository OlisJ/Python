class MyClass:
    def __init__(self):
        self.public_variable="this is a public variable"

    def public_method(self):
        print("this is a public method")

my_class=MyClass()
print(my_class.public_method())