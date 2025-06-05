string_length= len("Hello World")
list_length=len([1,2,4,6,89])
tuple_length=len((1,5,4))

print(string_length)
print(list_length)
print(tuple_length)

int_numbers=abs(-5)
com_numbers=abs(-3.14)

print(int_numbers)
print(com_numbers)

num_list=sorted([4,5,1,8])
str_exp=sorted("Apple")

print(num_list)
print(str_exp)

max_int=max([1,5,2,8,6])
max_str=max("polymorph")

print(max_int)
print(max_str)

min_int=min([1,5,2,8,6])
min_str=min("polymorph")

print(min_int)
print(min_str)


def add(x,y):
    return (x+y)

def concatenate(x,y):
    return str(x) + str(y)

def subtract(x,y):
    return (x-y)

def multiply (x,y):
    return (x*y)

def operator(operation, x,y):
    return operation(x,y)



result_sum=operator(add,5,2)
result_con=operator(concatenate,"Hello", "Alban")
result_mult=operator(multiply, 5,5)
result_sub=operator(subtract,2,1)


print(result_sum)
print(result_con)
print(result_mult)
print(result_sub)


