# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 10:25:09 2017

@author: nauge
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
#from matplotlib import cm  
#from matplotlib.ticker import LinearLocator, FormatStrFormatter  

fig=plt.figure()
ax=Axes3D(fig)
#fig=plt.gcf()

#line=ax.plot([],[],[])[0]

x=np.arange(-20,20,0.2)
y=np.arange(-20,20,0.2)
X,Y=np.meshgrid(x,y)

def z(x,y,t):
    Z=np.sin(((x)**2+(y)**2-10*t))
    return Z
#data=[z(i) for i in t]

#data=[z(x,i,j) for i in x]
lines=[ax.plot([],[],[],'b',lw=0.2)[0] for i in range(200)]


ax = fig.gca(projection='3d')  
def animate(num,lines):
    global data
    global x
    global y
    for j,line in enumerate(lines):
        
       
        Z=z(x,(j-100)/10.0,num/10.0) 
        y=[(j-100)/5.0]*200
        line.set_data(x,y)
        line.set_3d_properties(Z)
 #       fig.colorbar(line)
    return lines

ax.set_xlim3d([-20.0, 20.0])
ax.set_xlabel('X')

ax.set_ylim3d([-20.0, 20.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 2.0])
ax.set_zlabel('Z')

ax=fig.gca(projection='3d')
#ax.zaxis.set_major_locator(LinearLocator(10))  
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
#surf = ax.plot_surface(X, Y, z(X,Y,0), rstride=1, cstride=1, cmap=cm.jet,  
        #        linewidth=0, antialiased=False) 


 
anim=an.FuncAnimation(fig,animate,50,fargs=(lines,),interval=10,blit=False)
#fig.colorbar(surf, shrink=0.5, aspect=5)  
plt.show()


