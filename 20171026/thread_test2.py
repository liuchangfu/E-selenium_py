#单线程任务
import time

def music(func,loop):
    for i in range(loop):
        print("I was listenging music %s %s" % (func,time.ctime()))
        time.sleep(2)

def move(func,loop):
    for i in range(loop):
        print("I was watching move %s %s" % (func,time.ctime()))
        time.sleep(3)

if __name__=="__main__":
    music("爱情买卖",2)
    move("龙之战",2)
    print("All times:", time.ctime())