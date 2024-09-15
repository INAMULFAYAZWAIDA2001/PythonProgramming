for i in range(1, 101, 1):
    print(i, end=" ")

    if (i == 50):
        break
    else:
        print("fuck you")
print("Yeah, Still FUCK YOU")

#continuestatement

for i in [1,2,3,4,6,8,0]:
    if (i%2 != 0):
        continue
    print(i)