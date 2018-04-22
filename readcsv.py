# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:00:44 2017

@author: nauge
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import leastsq

csvfile = file('E:\\lecturefile\\lecture\\physical experiment\\semiconductor\\tek0005.csv', 'rb')
reader = csv.reader(csvfile)
ydata0=[]

for i,line in enumerate(reader):
    if i<4000:
        pass
    else:
        if len(line)==2:
           ydata0+=[float(line[1])]  
           
           
x=np.arange(0,len(ydata0)*4*10**-8,4*10**-8)
plt.plot(x,ydata0,'b',label='data')

def func(x,p):
    A,lamda,c2=p
    return A*np.exp(-lamda*x)+c2

def residuals(p,y,x):
    return y-func(x,p)

P0=[0.0,1.0,0.0]
plsq = leastsq(residuals, P0, args=(ydata0, x))
plt.plot(x,func(x,plsq[0]),'r',label='simulate')

string='GeAs2,Vol=6.09V\n'+'n*exp(-lamda*t)+c2'
string=string.replace('n',str(round(plsq[0][0],3)))
string=string.replace('lamda',str(round(plsq[0][1],3)))
string=string.replace('c2',str(round(plsq[0][2],3)))

plt.title(string)

plt.xlabel('time')
plt.ylabel('signal')
plt.legend()

plt.show()