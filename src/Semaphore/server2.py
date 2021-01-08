import threading
from  time import sleep
sem = threading.Semaphore()

def parent():
    
    sem.acquire()
    
    print("Waiting for Children")
        
    sem.release()
    sleep(1.5)
    while not sem.acquire(blocking=False):
        print("Parent Waiting")
        sleep(1)
    else:
        print("Parent finished")
    sem.release()
    

def child1():
    print("Hello from child #1")
    while not sem.acquire(blocking=False):
        print("Child #1 No Semaphore available")
        sleep(1)
    else:
        print("Child #1 I'm done with Semphore")
        
    sem.release()

def child2():
    print("Hello from child #2")
    while not sem.acquire(blocking=False):
        print("Child #2 No Semaphore available")
        sleep(1)
    else:
        print("Child #2 I'm done with Semphore")
        
    sem.release()

t = threading.Thread(target = parent)
t.start()
t2 = threading.Thread(target = child1)
t2.start()
t3 = threading.Thread(target = child2)
t3.start()
