list1=[1,2,3,4,5,6,7,8]
list2=["Green","Yellow","Pink"]



print(list1)
print(list2)


print(len(list2))
print(len(list1))

details = ["Inaam", 18, "Score", 9.8]
print(details)

print(list2[2])
print(list1[-4])
print(list1[0])
print(details[2])


print(list1[1:4])
print(list2[-2:-1])


print(list1[3:])
print(list2[1:])

print(list2[:2])
print(list1[:6])


print(list1[::3])
print(list1[1:5:2])
print(list1[1:7:3])






if "Yellow" in list2:
    print("Color is present")
else:
    print("Yellow not present")



names = ["Inaam", "Prateek", "shivam", "Prasad", "Charan", "Ajith"]

names_i=[item for item in names if (len(item)>4)]
names_o=[item for item in names if "a" in item]

print(names_i)
print(names_o)
