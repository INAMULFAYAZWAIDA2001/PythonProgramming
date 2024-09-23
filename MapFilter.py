#MAP
# def cube(x):
#     return x*x*x
l = [1,2,3,4,5,6,7]
newl = []

# for item in l:
#     newl.append(cube(item))

newl = list(map(lambda x:x*x*x, l))

print("Origional List: ", l)
print("Cube of the list: ", newl)

newL= list(filter(lambda x:x>2, l))
print("Filtered List: ", newL)