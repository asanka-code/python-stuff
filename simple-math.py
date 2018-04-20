#!/usr/bin/python

############################################
#					   #
# Program: simple-math.py		   #
# Author: Asanka Sayakkara		   #
# Description:				   #
#	This script demonstrates the basic #
#	methematical functionalities with  #
#	Python.				   #
#					   #
############################################

import math

print("==Simple Mathematics==")

ans = float(15)/3
print(ans)

print("The objects in 'math' package")
print(dir(math))

print("Information on a specific object")
#help(math.exp)

e = math.exp(1.0)
print("e=%f" % e)

print("pi=%f" % math.pi)

print("cos(0)=%f" % math.cos(0))
print("cos(90)=%f" % math.cos(math.pi/2))

print("log10(10)=%f" % math.log(10, 10))
print("log10(100)=%f" % math.log(100, 10))

