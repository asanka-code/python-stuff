# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:42:14 2018

@author: asanka
"""

# sudo apt install python-sympy

import sympy

# A simple equation
x = sympy.Symbol('x')
y = sympy.Symbol('y')
y = 2*x -x
print(y)

# An equation with variables assigned to some values.
a, b, c = sympy.symbols('a,b,c')
y = (2*a + 3*b + c)
print(y.subs(a, 1).subs(b, 2).subs(c, 3))

