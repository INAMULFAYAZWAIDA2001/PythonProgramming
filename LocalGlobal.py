x=10 #Global Variable

def funtion():
    y=5 #Local Variable
    global x #Changes the global variable value
    x=100
    print(y)

funtion()
print(x)