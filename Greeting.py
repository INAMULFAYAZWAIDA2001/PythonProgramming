import time

timestamp = time.strftime('%H')
timestamp = int(input("What Hour is it: "))

if(timestamp>6 and timestamp < 12):
    print("Good morning")
elif(timestamp > 12 and timestamp < 18):
    print("good afternoon")
if(timestamp>18 and timestamp<22):
    print("Good Evening")

