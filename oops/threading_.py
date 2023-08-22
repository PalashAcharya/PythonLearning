from threading import Thread
from time import sleep

def Run():
    for i in range(5):
        print("Running 1")
        sleep(1)

def run2():
    for i in range(5):
        print("Running 2")
        sleep(1)

class A(Thread):
    def run(self):
        print("Running A")
        sleep(1)

class B(Thread):
    def run(self):
        print("Running B")
        sleep(1)
#Run()
#run2()
thread = Thread(target=Run)  #thread = Thread(target=Run,args="If arguments present") argument expects a tuple as it is immutable
thread2 = Thread(target=run2)
thread3 = A()
thread4 = B()
thread.start()
thread2.start()
#thread3.start()
#thread4.start()
thread.join()
thread2.join()
#thread3.join()
#thread4.join()
print("Execution complete")