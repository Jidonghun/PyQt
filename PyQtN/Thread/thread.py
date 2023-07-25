from threading import Thread
import time

def task_a(value):
    for i in range(value):
        print('Thread - Task A:', i)
        time.sleep(2)
    print('A Task End')  
      
threadA = Thread(target = task_a, arg=(5,))
threadA.start()

for i in range(5):
    print('Main Task:', i)
    time.sleep(1)
    
print('---Main task end ---')
threadA.join()

for i in range(5):
    print('call me:', i)
    time.sleep(2)
print('A Task B')


