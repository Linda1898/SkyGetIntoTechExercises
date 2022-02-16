#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

for i in range(0, len(Belgium)):
    print("-", end=" ")



print("\n",Belgium.replace(",", ":"))

Belgium_split = Belgium.split(",")
print("\n",int(Belgium_split[1]) + int(Belgium_split[3]))