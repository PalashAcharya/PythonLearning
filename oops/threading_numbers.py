import threading
from time import sleep
def sum():
    j=0
    for i in range(1,6):
        print(i)
        j = j+i
        sleep(1)
    print(j)

def factorial(num):
    mul =1
    for i in range(1,num+1):
        print(i)
        mul = mul*i
        sleep(1)
    print(mul)
thread = threading.Thread(target=sum)
thread2 = threading.Thread(target=factorial,args=(5,))
thread.start()
thread2.start()
thread.join()
thread2.join()
#print(sum())
#print(factorial(5))
print("Executed")