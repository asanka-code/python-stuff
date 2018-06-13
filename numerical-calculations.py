#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:58:07 2018

@author: asanka
"""

import numpy as np

# Numpy array initializations
x = np.array([10, 20, 30, 40])
print(x)
x = np.arange(1, 2, 0.25)
print(x)
x = np.zeros(5)
print(x)

# Numpy Array elements can be updated
x[0] = 10
x[2] = 30
print(x)

# Select a range of numpy array elements
print("")
print("Selecting Ranges x[start_index:end_index]")
print(x[0:3])
print(x[1:3])

# Defining metrices as numpy arrays
print("")
print("Matrices")
x = np.array([ [1,2,3], [4,5,6] ])
print(x)
x = np.zeros((5,6))
print(x)

# Accessing matrix elements
print("")
print("Assigning values to matrix elements")
x[0,0] = 10
x[0,1] = 20
x[0,2] = 30
x[1,0] = 40
x[1,1] = 50
x[1,2] = 60
print(x)

print("")
print("All the rows but first column")
print(x[:,0])

print("")
print("All the columns but first row")
print(x[0,:])

# Numpy arrays can be converted back to lists or tuples
print("")
x = np.array([1, 2, 3])
print(x)
print(list(x))
print(tuple(x))




