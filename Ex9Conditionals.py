#in Python if user doesn't type anything then it is 0 which is == to false. So below works because if name is true (as in there is content) it will work.
name = input("Type in your name: ")
if name:
    print(name)
else:
    print('There is nothing there')

# example 2

name = None
while name != "Linda":
    name = input('Type in your name: ')
    print ("<" + name + " >")

#ctrl r - replace
#ctrl d - duplicate
#ctrl q - getdocumentation
#TODO testing to do
