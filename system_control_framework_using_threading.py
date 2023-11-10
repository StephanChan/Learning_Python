#!/usr/bin/env python
# coding: utf-8

# In[4]:


# using multithreading to control hardwares
# using Queue to init hardware threads
# '__main__' using the main thread, every hardware has its own thread
# GUI input triggers in-queue action to the specified queue
# define structure for queue element

import threading
import time
import sys
from multiprocessing import Queue

global XstageQueue
global YstageQueue
global AcqQueue
global GPUQueue
global SaveQueue

XstageQueue = Queue()
YstageQueue = Queue()
AcqQueue = Queue()
GPUQueue = Queue()
SaveQueue = Queue()

class moveto():
    def __init__(self, direction, destination):
        super().__init__()
        self.action='move to'
        self.direction=direction
        self.destination=destination
        
class setSpeed():
    def __init__(self, direction, speed):
        super().__init__()
        self.action='set speed'
        self.direction=direction
        self.speed=speed
        
class save():
    def __init__(self):
        super().__init__()
        self.action='save'
        
class process():
    def __init__(self):
        super().__init__()
        self.action='process'

class ACQ():
    def __init__(self, mode):
        super().__init__()
        self.action='acquire'
        self.mode=mode
        
class EXIT():
    def __init__(self):
        super().__init__()
        self.action='exit'
        
class SaveThread(threading.Thread):
    def __init__(self, work):
        super().__init__()
        self.work = work
        self.queue = SaveQueue
        
    # run 
    def run(self):
        self.QueueOut()
        
    def QueueOut(self):
        self.item = self.queue.get()
        while self.item.action != 'exit':
            print('Save thread is doing ',self.item.action)
            time.sleep(self.work)
            self.item = self.queue.get()
            
class ACQThread(threading.Thread):
    def __init__(self, work):
        super().__init__()
        self.work = work
        self.queue = AcqQueue
        
    def run(self):
        self.QueueOut()
        
    def QueueOut(self):
        self.item = self.queue.get()
        while self.item.action != 'exit':
            print('ACQ thread is doing ',self.item.action)
            time.sleep(self.work) 
            self.item = self.queue.get()
            
class GPUThread(threading.Thread):
    def __init__(self, work):
        super().__init__()
        self.work = work
        self.queue = GPUQueue
        
    def run(self):
        self.QueueOut()
        
    def QueueOut(self):
        self.item = self.queue.get()
        while self.item.action != 'exit':
            print('GPU thread is doing ',self.item.action)
            time.sleep(self.work)
            self.item = self.queue.get()

class XstageProcess(threading.Thread):
    def __init__(self, work):
        super().__init__()
        self.work = work
        self.queue = XstageQueue
    
    def run(self):
        self.QueueOut()
        
    def QueueOut(self):
        self.item = self.queue.get()
        while self.item.action != 'exit':
            print('X stage process is doing ',self.item.action)
            time.sleep(self.work)
            self.item = self.queue.get()

class YstageProcess(threading.Thread):
    def __init__(self, work):
        super().__init__()
        self.work = work
        self.queue = YstageQueue
        
    def run(self):
        self.QueueOut()
        
    def QueueOut(self):
        self.item = self.queue.get()
        while self.item.action != 'exit':
            print('Y stage process is doing ',self.item.action)
            time.sleep(self.work)
            self.item = self.queue.get()

if __name__ == '__main__':
    # assign sleep time to each hardware thread to simulate hardware working time
    Save_thread=SaveThread(5)
    ACQ_thread=ACQThread(10)
    GPU_thread=GPUThread(8)
    Xstage_process = XstageProcess(0.5)
    Ystage_process = YstageProcess(0.6)
    # start all threads
    Save_thread.start()
    ACQ_thread.start()
    GPU_thread.start()
    Xstage_process.start()
    Ystage_process.start()
    
    # put actions into the each queue
    ii=0
    while ii<5:
        an_element=save()
        SaveQueue.put(an_element)
        time.sleep(0.001)
        an_element=ACQ('single frame')
        AcqQueue.put(an_element)
        time.sleep(0.001)
        an_element=process()
        GPUQueue.put(an_element)
        time.sleep(0.001)
        an_element=moveto('up','10')
        XstageQueue.put(an_element)
        time.sleep(0.001)
        an_element=setSpeed('up','10')
        YstageQueue.put(an_element)
        time.sleep(0.001)
        ii+=1
    
    exit_elment=EXIT()
    SaveQueue.put(exit_elment)
    AcqQueue.put(exit_elment)
    GPUQueue.put(exit_elment)
    XstageQueue.put(exit_elment)
    YstageQueue.put(exit_elment)
    
    Save_thread.join()
    ACQ_thread.join()
    GPU_thread.join()
    Xstage_process.join()
    Ystage_process.join()
    
            
    


# In[ ]:




