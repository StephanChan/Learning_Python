from PyDAQmx import *
import numpy as np
from PyQt5.QtWidgets import *

import ctypes
import time
import sys


data=np.array([1,0,1,0],dtype=np.uint8)
task=Task()
task.CreateDOChan("/Dev1/port0/line0", "main", DAQmx_Val_ChanForAllLines)
task.CfgSampClkTiming("", 2, DAQmx_Val_Rising,
                              DAQmx_Val_ContSamps, 2)

task.CfgDigEdgeStartTrig("/Dev1/PFI9", DAQmx_Val_Falling)
#task.AutoRegisterDoneEvent(0)
task.WriteDigitalLines(2, 0, 10.0, DAQmx_Val_GroupByChannel,
                            data, None, None)

task.StartTask()
time.sleep(4)
task.StopTask()

