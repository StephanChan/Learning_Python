'''to stop one process while keep other proccesses running, cannot use join(), since this would
 block the main thread to wait for the stopped process terminates. since other processes' restart execute in main proccess,
 this would stop other processes.
the same works for threading'''
import numpy as np
import multiprocessing as mp
import time

def print_(num):
    for i in range(5):
        print('1 function %d %d' % (num,i))
        time.sleep(1)

def print_1(num):
    for i in range(5):
        print('2 function %d %d' % (num,i))
        time.sleep(1)

if __name__=='__main__':
    pool=[]
    #start=time.time()
    '''for i in range(2):
        p = mp.Process(target=print_, args=(i,))
        pool.append(p)
        
    for i in range(2):
        p = mp.Process(target=print_1, args=(i,))
        pool.append(p)
        #print_(i)'''
    p1 = mp.Process(target=print_, args=(1,))
    p2 = mp.Process(target=print_1, args=(2,))
    for i in range(10):
        pool=[]
        print("round %d"%i)
        if not p1.is_alive():
            p1 = mp.Process(target=print_, args=(1,))
            pool.append(p1)
        if not p2.is_alive():
              p2 = mp.Process(target=print_1, args=(2,))
              pool.append(p2)
        for j in pool:
            j.start()
        '''for j in pool:
            j.join()'''
        time.sleep(6)
        #p1.join()

    #stop=time.time()
    #print(stop-start)