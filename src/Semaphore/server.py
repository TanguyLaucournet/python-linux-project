import threading
import time

sem = threading.Semaphore()

def parent():

    sem.acquire()
    print("Wait for Child to Print")
    sem.release()
    time.sleep(0.5)
    sem.acquire()
    print("Child printed")
    sem.release()

def child():

    sem.acquire()
    print("Hello from Child")
    print("I am done! Release Semaphore")
    sem.release()
    time.sleep(0.25)

t = threading.Thread(target = parent)
t.start()
t2 = threading.Thread(target = child)
t2.start()