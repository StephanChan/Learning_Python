# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:02:18 2017

@author: nauge
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.ticker import LinearLocator, FormatStrFormatter  

fig=plt.figure()
#ax=fig.gca(projection='3d')
ax=Axes3D(fig)

x=np.arange(-10,10,0.1)
y=np.arange(-10,10,0.1)
X,Y=np.meshgrid(x,y)

def z(t):
    Z=np.sin(X**2+Y**2-10*t)
    return Z

Z=z(3)
ax.set_zlim3d([-2,2])
ax.set_zlabel('Z')

#ax.zaxis.set_major_locator(LinearLocator(10))  
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f')) 
surf=ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  cmap=cm.jet, linewidth=0)
plt.colorbar(surf, shrink=0.4, aspect=5)
plt.show()