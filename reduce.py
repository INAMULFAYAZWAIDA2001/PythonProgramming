from functools import reduce
numbers = [1,2,3,4,5,6]

def mysum(x,y):
    return x+y
sum  =  reduce(mysum, numbers)
print(sum)