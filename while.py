count = 5
while (count > 0):
    print(count)
    count=count-1


x = int(input("Enter the Number: "))
while(x<10):
    print(x)
    x=x-1
else:
    print("Counter is 0")

#emulate DoWhile

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break