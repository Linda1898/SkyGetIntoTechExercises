a= [1, "hello",[1,2,3,4], ['apples', 'oranges']]
# print (a[3][1])
# del a[0:2]
# print(a)

a.insert(2,"insert")
print(a)
print(a.pop(2))
a[3:3]=["harrow"]
print(a)
a.remove('harrow')
print(a)
print(a.pop(3))

opened_file = open('MyFile.txt', 'r')
for line in (opened_file):
    print(line, end="")
opened_file.close()