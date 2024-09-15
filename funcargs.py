#default arguments

def name (fname, mname = "John", lname= "Watson"):
    print("Hello,", fname, mname, lname)

name("Amy")

#keyword arguments

def name(fname,mname,lname):
    print("Hello,", fname,mname,lname)

name(mname= "Fayaz", lname="Waida", fname= "Inaam")

#required arguments

def name(fname, mname, lname):
    print("Hello,", fname,mname,lname)
name("Sheikh","Sadaf","Reyaz")


Variable-Lenght Arguments

a * before the parameter > Arbitrary Argument
a ** before the parameter > Keyword Arbitrary Argument

def name(*name):
    print("Hello",name[0], name[1], name[2])
name("Inamul", "Fayaz", "Waida")


def name(**name):
    print("Hello",name["fname"], name["mname"], name["lname"])
name(fname="Inamul", mname="Fayaz", lname="Waida")

