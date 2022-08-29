#multithreading
# thread-it is the smallest unit that can schedule-light weight process
import threading
import time    #delay tym to get in thread printing
def cal_square(num):
    print("calculate the square")
    for n in num:
        time.sleep(0.3)
        print("square",n*n)
def cal_cube(num):
    print("calculate the cube")
    for n in num:
        time.sleep(0.6)
        print("cube",n*n*n)
a=[3,4,5,6]
t1=threading.Thread(target=cal_square,args=(a,))
t2=threading.Thread(target=cal_cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()

