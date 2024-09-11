#IF - ELSE

# applePrice = int(input("Cost of apples:"))
# budget = int(input("My Budget: "))

# if (applePrice <= budget):
#     print("Alexa, add 1 kg apples to the cart.")
# else:
#     print("Alexa, do not add apples to the cart.")


#IF-ElIF


# num = int(input("Enter Number: "))

# if(num < 0):
#     print("Number is negative.")
# if(num == 0):
#     print("Number is zero.")
# else:
#     print("Number is Positive.") 



#NestedIF

num = int(input("Enter Number: "))

if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

