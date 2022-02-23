print("Q 2-4")
pelican = open("pelican.txt","r")
print('The data type of pelican is: ', type(pelican))
pelicanContents = pelican.read()
print("The data type of pelicanContents is: ",type(pelicanContents))
# print(pelicanContents)
# #TODO difference between q3 display the type of the returned data vs q 4 what data type is the output?

print("Q 5-6")

#TODO why only one works at a time? And why does the question ask to put into a list and
# then print but says printing a for lop from readlines is inefficient and instead recommends the abc version below?-slide 5
#Lexie has done split() for exercise below
pelicanLineList = pelican.readlines()
print("There are", len(pelicanLineList), "lines in the text.\n")
for line in pelicanLineList :
    print(line, end="")

print("TO DO LIST EXAMPLE")

for abc in pelican:
    print(abc, end="")
pelican.close()

