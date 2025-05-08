my_set={1,2,3,4,5,5,5,6,6,7,8}
print(my_set)
new_set=set([1,2,3,3,4,4])
print(new_set)
A={1,2,3}
B={3,4,5}
#find the union
unioni= A.union(B) # unioni = A|B
print(unioni)

#Intersection
prerja= A.intersection(B) # prerja =A &B
print(prerja)

#differenca
diferenca = A.difference(B) # diferenca = A-B
print(diferenca)

#diferenca simetrike
d_simetrike = A.symmetric_difference(B) #d_simetrike= A ^B
print(d_simetrike)

#add element
A.add(6)
print(A)

#remove
A.remove(6)
print(A)

#discard-remove element without error if does not exist
A.discard(100)

#removes all elements
A.clear()

#find length number of elements
print(len(A))

lista=[1,1,2,2,3,3]
C=set(lista)
print(C)

X={"a",'b',"c"}
Y={'c','d','e'}

tr=X & Y
print(tr)

O={1,2,3,4,5}
numri=3
print(numri in O)