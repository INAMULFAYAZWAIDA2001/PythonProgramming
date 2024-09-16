'''SINCE TUPLES ARE IMMUTABLE WE HAVE 
TO CONVERT THEM IN LISTS FIRST TO OPERATE 
ON THEM'''


num = (1,2,3,4,5,5,5,56)
temp = list(num)

temp.append(112) #------adds item
temp.pop(2)  #-----removes item
temp[2]="Inam" #---change item
num=tuple(temp)
print(num)


count = num.count(5)
print("count of 5 in num is: ", count)

index = num.index(1)
print("First occurance of item 1 is at index: ", index)