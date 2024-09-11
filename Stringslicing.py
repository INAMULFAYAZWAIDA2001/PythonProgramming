fruit = "Banana"
BananaLen = len(fruit)
print("Banana is a", BananaLen, "letter word.") 

print(fruit[0:5]) #including 0 but not 5
print(fruit[1:5])
print(fruit[:5]) # By default 0
print(fruit[0:-4]) #print(fruit[0: len(fruit) - 4])
print(fruit[-3:-1])
print(fruit[2:]) #slices till the end 
print(fruit[0:])

name = "Inaam"
for i in name:
    print(i)


nm = "Inaam"
len1 = len(nm)
print(len1)

print(nm[-4:-2])