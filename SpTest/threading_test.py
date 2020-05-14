import threading
import time
import requests


class MyThreading(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        Text()
        print(self.name+'1')

def Text():
    code = requests.get('https://www.baidu.com').status_code
    print(str(code) + str(time.time()))

thread1 = MyThreading('11')
thread2 = MyThreading('22')

list1 = []
list1.append(thread1)
list1.append(thread2)

for t in  list1:
    t.start()

for i in list1:
    i.join()


print ("退出主线程")