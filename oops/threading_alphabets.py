import threading 
from time import sleep
class Alphabet(threading.Thread):                
    def run(self):
        ch = 97
        while(ch!=123):
            print("Lowercase Character:",chr(ch))
            ch=ch+1
            sleep(1)
def Uppercase():
    ch = 65
    while(ch!=91):
        print("Uppercase Characters:",chr(ch))
        ch = ch+1
        sleep(1)
thread = Alphabet()
thread2 = threading.Thread(target=Uppercase)
thread.start()
thread2.start()
thread.join()
thread2.join()