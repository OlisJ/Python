from email.policy import default

from pyexpat.errors import messages

total=0

for number in range(1,11):
    if number%2==0:
        total+number
print("the sum of even numbers from 1 to 10 is ", total)

#this is defining a function

def greet():
    print('hello world!')
#this is how we use a function
greet()

def greet_person(name):
    print('hello', name)

greet_person("ramadan")



def shuma(x,y):
    z=x+y
    return z
result=shuma(2,4)
print('2+4=',result)

#local variables
def greet(name):
    message=f"hello,{name}"
    print(message)

greet('Hajdar')



#argumentet dhe definimi i tyre
def greet_person(name, greeting="Hello"):
    message=f"{greeting},{name}"
    return message
default_greeting= greet_person('Alma')
print(default_greeting)

custom_greeting=greet_person("alma","Good Morning")
print(custom_greeting)

pershendetje="hi"
def greet_people(name):
    global pershendetje
    return f"{pershendetje},{name}"
variabla=greet_people("alma")
print(variabla)