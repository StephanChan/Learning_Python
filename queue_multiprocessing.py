# Written by Vamei
import os
import multiprocessing
import time
#==================
# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    lock.release()
#===================
# Main
record1 = []   # store input processes
record2 = []   # store output processes
lock  = multiprocessing.Lock()    # To prevent messy print
queue = multiprocessing.Queue(4)#########queue capacity is only 4

# input processes
for i in range(4):
    process = multiprocessing.Process(target=inputQ,args=(queue,))
    process.start()
    record1.append(process)

for p in record1:#########when total processing number is <=queue, all processes can finish when joined before deque happened
    p.join()     #########but if queue capacity is less than process number, if joined here, exass processes cannot proceed since queue is full
                 #########in that case, join must be put after deque processing happened.



# output processes
for i in range(4):
    process = multiprocessing.Process(target=outputQ,args=(queue,lock))
    process.start()
    record2.append(process)

queue.close()  ######## No more object will come, and no more object can come out of the queue, close the queue


for p in record2:
    p.join()