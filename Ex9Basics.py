firstName = "Linda"
lastName= "Jackson"
print(firstName, " ", lastName)
listNames=[firstName,lastName]
print(listNames)
dictNames={"first":firstName, "last":lastName}
print(dictNames)
# print(dictNames[lastName]) CREATES KEY ERROR because listing value not key?


print(listNames[0] + " " + listNames[1])
print(dictNames["first"] + " " + dictNames["last"])

var=input("Please enter a value: ")
print(var.upper())
print(len(var))
print(var.isdecimal())