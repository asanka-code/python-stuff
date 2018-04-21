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

print("==File Input and Output==")

# Writing to a file to write
myFile = open("temp.txt", "w")
myFile.write("Here's the first line\n")
myFile.write("Here's the second line\n")
myFile.write("Here's the third line\n")
myFile.close()

# Reading from a file
myFile = open("temp.txt", "r")
text = myFile.read()
print("File content: %s" % text)
myFile.close()

myFile = open("temp.txt", "r")
textLines = myFile.readlines()
print("The Lines: %s" % text)
myFile.close()

myFile = open("temp.txt", "r")
textLines = myFile.readlines()
for line in textLines:
	print("Line: %s" % line)
myFile.close()



