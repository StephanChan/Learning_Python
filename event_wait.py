from threading import Event
from threading import Thread
import time

def event_wait(event_):
    #time.sleep(1)
    print('do something')
    event_.wait()
    print('do something after block')

def event_set(event_):
    print('set event')
    event_.set()

if __name__=='__main__':
    aevent=Event()
    time.sleep(2)
    athread=Thread(target=event_wait, args=(aevent,))
    athread.start()
    time.sleep(1)
    anothread=Thread(target=event_set,args=(aevent,))
    anothread.start()