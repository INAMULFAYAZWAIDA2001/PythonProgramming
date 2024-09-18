# try:
#     num=int(input('Enter an integer:  '))
# except ValueError:
#     print('Number entered is not an integer')


# try:
#     num = int(input('Enter an Integer: '))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print('Number entered is not an integer')
# except IndexError:
#     print('Index Error')


# a = input('Enter the number: ')
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)}X{i} = {int(a)*i}")
# except:
#     print('Invalid Input!')

# finally:
#     print("This block is always executed")

def func1():
    try:
        l=[1,2,3,4]
        i = int(input('Enter the index: '))
        print(l[i])
        return 1 
    except IndexError:
        print('Some Error Occured')
        return 0
    finally:
        print('I am always executed')

x = func1()
print(x)