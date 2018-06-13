# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Wed Jun 13 15:41:08 2018

@author: asanka
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3.14, 3.14, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(5,5))
plt.subplot(2,1,1)
plt.plot(x,y1,label="sin(x)")
plt.plot(x,y2,label="cos(x)")
plt.xlabel('x')
plt.legend()
plt.grid()
plt.title("The Title of the Graph")

plt.subplots_adjust(wspace=0, hspace=0.5)

plt.subplot(2,1,2)
plt.plot(x,y1,label="sin(x)")
plt.plot(x,y2,label="cos(x)")
plt.xlabel('x')
plt.legend()
plt.grid()
plt.title("The Title of the Graph")

plt.show()
#plt.savefig("myplot.pdf")
