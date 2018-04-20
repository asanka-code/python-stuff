#!/usr/bin/python

############################################
#					   #
# Program: data-types.py		   #
# Author: Asanka Sayakkara		   #
# Description:				   #
#	This script demonstrates the basic #
#	data types available on python.    #
#					   #
############################################

import cmath # for complex number mathematics

print("==Data Types==")

a = 45
print(type(a))

c = [10, 32, 49]
print(type(c))

print("A string to a float")
a = '23.86'
print(type(a))
a = float(a)
print(type(a))

# Dealing with complex numbers
print("Complex Numbers")
b = 2 + 3j
print(type(b))
print(b.real)
print(b.imag)

print(dir(cmath))
c = cmath.sqrt(b)
print(c)

# Handling lists
print("Processing lists")
mylist1 = [23, 43, 56, 62, 40]
mylist2 = [93, 39, 48]
print(mylist1)
print(mylist2)

newlist = mylist1 + mylist2
print(newlist)
newlist.append(100)
print(newlist)
newlist.remove(62)
print(newlist)

print("Range starting from 1 to less than 10")
print(range(1, 10))
print("Range from 1 to less than 10 in 2 value steps")
print(range(1, 10, 2))

for i in range(0, 10):
	print(i)

# slicing a list
print("Slicing Lists")
mylist = range(1, 21)
print(mylist)
print(mylist[0:10])
print(mylist[0:10:2])
print(mylist[1:10:2])

print("Odd places in the list")
print(mylist[0::2])
print("Even places in the list")
print(mylist[1::2])








