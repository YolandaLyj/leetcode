import threading
import time
lock = threading.RLock()
def my_print(name):
    for i in range(10):
        time.sleep(1)
        lock.acquire()
        print(name,i)
        lock.release()

start = time.time()#返回当前的时间戳
t1 = threading.Thread(target = my_print,args = ["threading1:"]) #传个任务,和参数进来
t2 = threading.Thread(target = my_print,args = ['threading2:'])
t1.start()#线程开始
t2.start()
t1.join()
t2.join()
end = time.time()
print(end-start)
print("结束")