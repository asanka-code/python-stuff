#!/usr/bin/python3

# This program demonstrates the capability of passing a function as a parameter
# to another function.

# Library function to acquire sliding windows 
def startSlidingWindow(windowSize, windowSteps, function, params):
	for i in range(0,5):
		# calling the function given as a parameter
		function(*params)

# Sample user defined function
def processWindow(a,b):
	print("param1: %d param2: %d" % (a,b))

# We are calling the library function along with the user defined function as a parameter
startSlidingWindow(10, 2, processWindow, (1, 2))

