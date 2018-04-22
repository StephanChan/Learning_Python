# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:12:37 2017

@author: nauge
"""

#coding=gbk
import matplotlib
matplotlib.use('WXAgg') # do this before importing pylab
import matplotlib.pyplot as pl
from doublependulm import d_pendulum, DoublePendulum

fig = pl.figure(figsize=(4,4))
line1, = pl.plot([0,0], [0,0], "-o")
line2, = pl.plot([0,0], [0,0], "-o")
pl.axis("equal")
pl.xlim(-4,4)
pl.ylim(-4,2)

pendulum = DoublePendulum(1.0, 2.0, 1.0, 2.0)
pendulum.init_status[:] = 1.0, 2.0, 0, 0

x1, y1, x2, y2 = [],[],[],[]
idx = 0

def update_line(event):
    global x1, x2, y1, y2, idx
    if idx == len(x1):
        x1, y1, x2, y2 = d_pendulum(pendulum, 0, 1, 0.05)
        idx = 0 
    line1.set_xdata([0, x1[idx]])
    line1.set_ydata([0, y1[idx]])
    line2.set_xdata([x1[idx], x2[idx]])
    line2.set_ydata([y1[idx], y2[idx]])
    fig.canvas.draw()                 
    idx += 1

import wx
id = wx.NewId()
d=fig.canvas.manager
actor = d.frame
timer = wx.Timer(actor, id=id)
timer.Start(1)
wx.EVT_TIMER(actor, id, update_line)
pl.show()
