# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:23:51 2017

@author: nauge
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
import matplotlib.animation as an



def Lorenz(w,t,a,b,c):
   x,y,z=w
   return np.array([a*(y-x),(b*x-x*z-y),(x*y-c*z)])

fig=plt.figure()
ax=p3.Axes3D(fig)  
line =ax.plot([],[],[],lw=0.5)[0]
               
def plotlorenz():
   
   a=10.0
   b=28.0
   c=3.0
   x0=0
   y0=1.0
   z0=0
   stime=0
   etime=90
   step=0.02
   track=odeint(Lorenz,[x0,y0,z0],np.arange(stime,etime,step),args=(a,b,c))
   
   return track
track=plotlorenz()

t=np.empty((3,len(track)))
for i in range(len(track)):
    t[:,i]=track[i][:]
        
def init():
    line.set_data([],[],[])
    return line,

def animate(num,track):
   line.set_data(track[0:2,:num])
   line.set_3d_properties(track[2,:num])
   
   return line,

ax.set_xlim3d([-20.0, 20.0])
ax.set_xlabel('X')

ax.set_ylim3d([-20.0, 20.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 35.0])
ax.set_zlabel('Z')



anim=an.FuncAnimation(fig,animate,5000,fargs=(t,),interval=1,blit=False)
plt.show()
            
