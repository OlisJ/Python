age=25
age_As_String=str(age)
print(age_As_String,"of type", type(age_As_String))

print(bool(0)) #this is false because 0 is false in boolean
print(bool(42)) #this is true because 42 translates to 1

print(bool(""))
print(bool('Hello World'))

#implicit type castin

x=32
y=5.3
resultati=x+y
print(resultati, 'of type', type(resultati))

c=4
resultati2="hello"*c
print(resultati2)

#get 2 numbers from user input and sum them up
num1=int(input("pick a number"))
num2=int(input("pick a number"))
resultati3=num1+num2
print(resultati3)