# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:08:38 2017

@author: nauge
"""
#coding=gbk
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as an 
from math import sin,cos
from scipy.integrate import odeint

g = 9.8
fig=plt.figure()
ax=plt.axes(xlim=(-3,3),ylim=(-3,1))
line1, =ax.plot([],[],'r',lw=1)
line2, =ax.plot([],[],'b',lw=1)
line3, =ax.plot([],[],'r',lw=1)
line4, =ax.plot([],[],'b',lw=1)


class DoublePendulum(object):
    def __init__(self, m1, m2, l1, l2):
        self.m1, self.m2, self.l1, self.l2 = m1, m2, l1, l2
        self.init_status = np.array([0.0,0.0,0.0,0.0])
        
    def equations(self, w, t):
        """
        微分方程公式
        """
        m1, m2, l1, l2 = self.m1, self.m2, self.l1, self.l2
        th1, th2, v1, v2 = w
        dth1 = v1
        dth2 = v2
        
        #eq of th1
        a = l1*l1*(m1+m2)  # dv1 parameter
        b = l1*m2*l2*cos(th1-th2) # dv2 paramter
        c = l1*(m2*l2*sin(th1-th2)*dth2*dth2 + (m1+m2)*g*sin(th1))
        
        #eq of th2
        d = m2*l2*l1*cos(th1-th2) # dv1 parameter
        e = m2*l2*l2 # dv2 parameter
        f = m2*l2*(-l1*sin(th1-th2)*dth1*dth1 + g*sin(th2))
        
        dv1, dv2 = np.linalg.solve([[a,b],[d,e]], [-c,-f])
        
        return np.array([dth1, dth2, dv1, dv2])
        
def d_pendulum(pendulum, ts, te, tstep):
    """
    对双摆系统的微分方程组进行数值求解，返回两个小球的X-Y坐标
    """
    t = np.arange(ts, te, tstep)
    track = odeint(pendulum.equations, pendulum.init_status, t)
    th1_array, th2_array = track[:,0], track[:, 1]
    l1, l2 = pendulum.l1, pendulum.l2
    x1 = l1*np.sin(th1_array)
    y1 = -l1*np.cos(th1_array)
    x2 = x1 + l2*np.sin(th2_array)
    y2 = y1 - l2*np.cos(th2_array)
    pendulum.init_status = track[-1,:].copy() #将最后的状态赋给pendulum
    return [x1, y1, x2, y2]

if __name__ == "__main__":    
    
    pendulum = DoublePendulum(5.0, 0.1, 1.0, 2.0) 
    th1, th2 = 1.2, 0
    pendulum.init_status[:2] = th1, th2
    x1, y1, x2, y2 = d_pendulum(pendulum, 0, 70, 0.01)
    #plt.plot(x1,y1, label = u"上球")
    #plt.plot(x2,y2, label = u"下球")
    def init():  
        
        line4.set_data([],[])
        return line4, 
  
    def animate(i,X1,X2,Y1,Y2): 
        x1=X1[i]
        x2=X2[i]
        y1=Y1[i]
        y2=Y2[i]
        
        line1.set_data(X1[:i],Y1[:i] )
        line2.set_data(X2[:i],Y2[:i])
        line3.set_data([0,x1],[0,y1])
        line4.set_data([x1,x2],[y1,y2])
        #line.plot(x1[:i],y1[:,i])
        #line.plot(x2[:,i],y2[:,i])
        return line1,line2,line3,line4,   
    anim = an.FuncAnimation(fig, animate,4000,
                            fargs=(x1,x2,y1,y2) ,  
                            interval=15, blit=False)  
    #plt.title(u"双摆系统的轨迹, 初始角度=%s,%s" % (th1, th2))
    #plt.legend()
    #plt.axis("equal")
    plt.show()