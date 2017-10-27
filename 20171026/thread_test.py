#单线程任务
import time

def music():
    print("I was listenging music %s" % time.ctime())
    time.sleep(2)

def move():
    print("I was watching move %s" % time.ctime())
    time.sleep(3)

if __name__=="__main__":
    music()
    move()
    print("All times:", time.ctime())