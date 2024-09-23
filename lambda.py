# def double(x):
#     return x*2
# print(double(5))

double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y: (x+y)/2
print(double(10))
print(cube(10))
print(avg(10,20))

def appl(fx, value):
    return 6+fx(value)
print(appl(lambda x:x*x,10))