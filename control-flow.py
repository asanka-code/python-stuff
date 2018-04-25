#!/usr/bin/python

############################################
#					   #
# Program: control-flow.py		   #
# Author: Asanka Sayakkara		   #
# Description:				   #
#	This script demonstrates the basic #
#	control flow functionalities with  #
#	Python.				   #
#					   #
############################################

# Conditional statements
x = -10

if x == 10:
    print("x is 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is greater than 10")

y = 20

if x > 10 and y < 50:
    print("x is greater than 10 and y is less than 50")
elif x < 10 and y < 50:
    print("x is less than 10 and y is less than 50")
else:
    print("Something else")

# Handling exceptions
try:
    z = y/0
except:
    print("Cought an exception")

