name_of_list=['item1','item2', 'item3', 'item4', 'item5']
shopping_list=["banane",3.5,3]
print(shopping_list[1])


lista_1=['blue','red','green','purple']
lista_1.append("black")# Adds element
#lista_1.clear() cleans all the elements
#lista_1.count() #counts the elements

lista_2=lista_1.copy() # copies the primary list
print(lista_1)
print(lista_2)

lista_1.insert(1,"pink")#adds element to a specific place
print(lista_1)

lista_2.pop(2) #removes the element in the specified place
print(lista_2)
lista_2.remove("red") #removes item based by value

lista_2.reverse() #reverses the elements

print(lista_2[-1])