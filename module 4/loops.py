#for loop
names=['alma','blerta','dhurata','shpati']
for name in names:
    print(name)

#shembulli 2
sentence_sh='Hello, world5'
for char in sentence_sh:
    if char.isalpha(): # kthen true or false if char is letter
        print(char)


#shembulli 3 w range func
for numri in range(1,6): #x fillon y mbarin nuk perfshin y
    print(numri)

#find max in list
numrat=[1,2,3,4,5,6,7,8,9,10,99]
max=numrat[0]
for num in numrat:
    if num>max:
        max=num
print('the max value of  the list is',max)