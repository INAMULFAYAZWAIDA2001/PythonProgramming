colors = ["Red","Blue","Orange","Pink"]
num = [0,1,2,3,4,6,2,1,4,2,8,4,5,6,7,8,9]

#----------------------------------------------------


num.sort()
num.sort(reverse=True)
print(num)


#----------------------------------------------------

colors.reverse()
print(colors)


#----------------------------------------------------

num.index(2)
print(num)


#----------------------------------------------------


num.count(4)
print(num)

#----------------------------------------------------

newlist = colors.copy()
print(colors)
print(newlist)

#----------------------------------------------------

num.append(69)
print(num)

#----------------------------------------------------

num.insert(7, 8)
colors.insert(3, "Violet")

#----------------------------------------------------

colors.extend(names)
print(colors)

#----------------------------------------------------

print(colors+names)