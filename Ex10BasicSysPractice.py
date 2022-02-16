#!/usr/bin/python
#Example Python Script
import sys
argc = len(sys.argv)
if argc > 1:
    print('Too many args')
else:
    where = 'World'
    print('Hello', where)

print ('Goodbye from ' + sys.argv[0])

#The first argument, sys.argv[0], is always the name of the program as it was invoked,
#and sys.argv[1] is the first argument you pass to the program.
# print(sys.argv) = ['C:/Users/linda/PycharmProjects/Exercise9/Anatomy.py'] there is no sys.argv[1] so it creates an error
