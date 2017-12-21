from PyDAQmx import *
import numpy
import time

# testing reading digital input

#Declaration of variable passed by reference
digital_input = Task()
read = int32()
num=int32()
data = numpy.zeros(10, dtype=numpy.uint32)
#data = numpy.zeros((1000,), dtype=numpy.float64)

#DAQ Configuration Code
digital_input.CreateDIChan("/Dev1/port0/line2","",DAQmx_Val_ChanForAllLines)
#digital_input.CfgSampClkTiming("", 20, DAQmx_Val_Rising, DAQmx_Val_ContSamps, 40)
digital_input.CfgSampClkTiming( "", 10.0, DAQmx_Val_Rising, DAQmx_Val_ContSamps, 10) #frequency should equal the input signal frequency
#DAQmx Start Code
digital_input.StartTask()
#print "Acquiring samples continuously. Press Ctrl+C to interrupt\n"

#DAQmx Read Code
i=0
while(True):
    digital_input.ReadDigitalU32(1, 10.0, DAQmx_Val_GroupByChannel, data, 1, byref(read), None)  #first arg: number of data read every time, should be 1   data type should be uint32
    #digital_input.ReadDigitalLines(4, 10.0, DAQmx_Val_GroupByChannel, data, 10, byref(read), byref(num),None)   #readDigitalLines: read several samples in a channel
    i+=1
    if data[0]!=0:
       print("get signal%d"%i)



