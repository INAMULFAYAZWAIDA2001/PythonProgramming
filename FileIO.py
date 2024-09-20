#READING A FILE
# f = open('myfile.txt', 'r')
# text = f.read()
# print(text) 

#Writing a file

f=open('myfile.txt', 'a')
f.write('Hello, Inam')
f.close()

with open('myfile.txt', 'a') as f:
    f.write('Hey I am inside with')