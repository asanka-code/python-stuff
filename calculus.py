# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:59:50 2018

@author: asanka
"""

import sympy

# Differentiation of an equation
x = sympy.Symbol('x')
y = sympy.Symbol('y')
y = x**9 + 3*x + 10
dydx = sympy.diff(y,x)
print(dydx)
print(dydx.subs(x,2))

# Integration of an equation
y = 9*x**8 + 3
inte = sympy.integrate(y,x)
print(inte)

