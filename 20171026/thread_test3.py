#多线程任务
import time
import threading


def music(func,loop):
    for i in range(loop):
        print("I was listenging music %s %s" % (func,time.ctime()))
        time.sleep(2)

def move(func,loop):
    for i in range(loop):
        print("I was watching move %s %s" % (func,time.ctime()))
        time.sleep(3)

threads = []
t1 = threading.Thread(target=music,args=("爱情买卖",2))
threads.append(t1)
t2 = threading.Thread(target=move,args=("龙之战",2))
threads.append(t2)


if __name__=="__main__":
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("all end",time.ctime())


