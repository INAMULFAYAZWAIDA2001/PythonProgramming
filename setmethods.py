num1 = {1,2,3,4,5,6,3,2,4,6}
num2 = {2,4,5,6,1,23,4,6,7,8}

num3 = num1.union(num2)
num4 = num1.intersection(num2)

num5 = num1.symmetric_difference(num2)
num1.symmetric_difference_update(num2)

num6 = num1.difference(num2)
num2.difference_update(num1)


print(num3)
print(num4)
print(num5)
print(num1)
print(num6)
print(num2)

print(num1.isdisjoint(num2))
print(num1.issuperset(num2))
print(num1.issubset(num2))

#--------------------------------

num = {1,2,2,2,3,4,5,6,2,1,3}
item = num.pop()
print(num) #1 was popped
print(item) 
num.clear()
print(num)

del num
print(num)


#----------------------------------


cities = {"India", "Tokyo", "China"}
cities.remove("India")
print(cities)

cities2={"USA","Germany"}
cities.update(cities2)
print(cities)

cities.add('India')
print(cities)

item = cities.pop()
print(cities)
print(f"My name is {item} and I was popped from{cities}")