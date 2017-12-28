# Learning
here's some files on what I'm learning, like multiprocessing

Comments:

multiprocessing_join.py  shows the use of join() in repeatly started processes condition. such also works in threading.

manager_multiprocessing.py  shows how to use manager to define shared variables by all the processes
                         since processes don't share global variables
                         
lines_alternately_share_variable_in_multiprocessing.py    shows that child process when starts within father process, can inherit the variable changed within father process. such case makes send_message and process_message(in my TSTORM software) multiprocessing version workable

queue_multiprocessing.py shows how to use queues. the point is the queue capacity and the in_queue processes number when using join()

all the files works on linux system, since in windows, multiprocessing can only be used after if __name__=="__main__":(not checked by myself, but all the googles say the same) I suggest not to use multiprocessing in windows.

how does multiprocessing deals with variables?  
     my guess, when new process starts, it copies all the variables and codes in the main process to their own memory. such explaination makes sense considering two facts: 
     1.processes cannot share variables; when the main process consists of initiating hardwares, the hardware will be multi initiated when processes starts
     2.when a new process starts within an old process, the new process have the variable changed by the old process, in a way that they seem to share that variable, which is the case in lines_alternately_share_variable_in_multiprocessing
     
ctypes: need to be learned
