# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:15:17 2017

@author: nauge
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from scipy.integrate import odeint

def Lorenz(w,t,a,b,c):
   x,y,z=w
   return np.array([a*(y-x),(b*x-x*z-y),(x*y-c*z)])

def plotlorenz():
   '''a=float(raw_input('a= '))
   b=float(raw_input('b= '))
   c=float(raw_input('c= '))
   x0=float(raw_input('x0= '))
   y0=float(raw_input('y0= '))
   z0=float(raw_input('z0= '))
   stime=float(raw_input('stime= '))
   etime=float(raw_input('endtime= '))
   step=float(raw_input('step= '))'''
   a=10.0
   b=28.0
   c=3.0
   x0=0
   y0=1.0
   z0=0
   stime=0
   etime=50
   step=0.02
   track=odeint(Lorenz,[x0,y0,z0],np.arange(stime,etime,step),args=(a,b,c))
   
   return track
track=plotlorenz()

'''x=[]
y=[]
z=[]
for i in range(len(track)):

    x+=[track[i,0]]
    y+=[track[i,1]]
    z+=[track[i,2]]'''

x=track[:,0]
y=track[:,1]
z=track[:,2]
def update_line(num, data, line,) :
    x,y,z=data
        # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(x[:num],y[:num])
    line.set_3d_properties(z[:num])
    return line,

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
line, = ax.plot([], [], [],lw=0.5)

# Setting the axes properties
ax.set_xlim3d([-20.0, 20.0])
ax.set_xlabel('X')

ax.set_ylim3d([-20.0, 20.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 35.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_line, 1000, fargs=([x,y,z], line),
                              interval=1, blit=False)

plt.show()