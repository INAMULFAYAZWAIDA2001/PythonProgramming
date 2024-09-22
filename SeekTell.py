#File Handling
# with open("sample.txt", 'r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data=f.read(5)
#     print(data)

with open('sample.txt' , 'w') as f:
    f.write("Hello Inaam!")
    f.truncate(4)
with open('sample.txt', 'r') as f:
    print(f.read())