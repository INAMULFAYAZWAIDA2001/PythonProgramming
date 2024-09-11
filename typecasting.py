a = "2"
a1 = 2 
b = "3"
b1 = 3

print(a1 + b1)
print(a + b)
print(int(a)+int(b))


string = "15"
number = 7
string_name = int(string) #throws an error if the string is not a valid integer

sum = number + string_name

print("The sum of both the numbers is : ", sum)




#implicit Typecasting

c = 1.9
print("The datatype of c is", type(c))
d = 8
print("The datatype of d is", type(d))
e = c + d
print(e)
print("The datatype of e is", type(e))