#!/usr/bin/python

############################################
#					   #
# Program: functions.py			   #
# Author: Asanka Sayakkara		   #
# Description:				   #
#	This script demonstrates the usage #
#	of functions in Python.		   #
#					   #
############################################

# A function which accepts parameters by value
def multi_para_function(a, b):
	a = 100
	b = 200
	#print("a=%d b=%d" % (a, b))

first=10
second=20
multi_para_function(first, second)
print("After the multi para function, first=%d second=%d" % (first, second))


# A function which accepts parameters by reference
def para_list_function(params):
	params[0] = params[0] + 100
	params[1] = params[1] + 200

params=[10, 20]
para_list_function(params)
print("After the para list function %s" % params)


def str_para_function(string):
	print("string=%s" % string)

myStr="Hello!"
str_para_function(myStr)







