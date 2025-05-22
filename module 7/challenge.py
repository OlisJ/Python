#Challenge
from multiprocessing.managers import Value
from traceback import print_tb

from babel.plural import negate


def det(nr1,nr2, operator):
    if operator=="+":
        print(nr1+nr2)
    elif operator=="-":
        print(nr1-nr2)
    elif operator=="/":
        print(nr1/nr2)
    elif operator=="*":
        print(nr1*nr2)
    else:
        raise ValueError("invalid operator")

det(6,4,"*")

#4
try:
    num1=float(input("Enter the first number" ))
    num2=float(input("Enter the second number"))
    operatori= input('Enter an operator +,-,*,/')
    resultati=calculate(num1,num2,operatori)
    print(f"the result of {num1} {operatori} {num2}is :{resultati}")
except ValueError as e:
    print(f"Invalid input {e}")
except ZeroDivisionError as e:
    print(f"cannot divide by 0 {e}")
except Exception as e:
    print(f"Error {e}")
finally:
    print("End of the program")