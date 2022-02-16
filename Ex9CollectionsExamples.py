MyList = ['apples', 'oranges', 'chocolate']
print(MyList)
print(type(MyList))
MyList[-1]='hashbrown'
MyTuple = ('apples', 'oranges', 'chocolate')
print(MyList[-1])
print(MyTuple[-1])
print(MyTuple)

for index_item, value in enumerate(MyList):
    MyList[index_item]=value+value
print (MyList)

#HW - exercise 10 plus calculator