#error handling Try, Except, Finally
#Try - writing of the needed code
#Except - what happens if an error occurs in the try part
#Finally - Part of code that is always run

#This is dedicated for errors that programmers do not predict
#first example
#try:
  #  print("Pjesto dy numra")
   # nr1=int(input("shkruaj nje numer"))
    #nr2=int(input("shkruaj numrin e dyt"))
    #resultati=nr1/nr2
    #print("rezultati", resultati)
#except ZeroDivisionError:
#    print("Ka je nis me zero ??")

#2nd example
fruits={
    "apples":5,
    "banannas":6,
    "oranges":7
}
try:
    print(fruits['cherry'])
except KeyError:
    print("THe key doesnt exist")


#3rd example
text="this is not a number"
try:
    text_to_int=int(text)
except Exception as e:
    print("An error has occurred while parsing the data", e)


#4th example
try:
    resultati=10/2
except ZeroDivisionError:
    print("division by zero error occurred")
else:
    print("Division successful," ,resultati)

#5th example
try:
    resultati=10/0
except ZeroDivisionError:
    print("division by zero error")
finally:
    print('this part of code always runs')



