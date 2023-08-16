import threading
import time
import multiprocessing

# def fun1(n):
#     for _ in range(n):
#         print(_,"this is fun one")
#         time.sleep(.5)  #wait .5 sec

# def fun2():
#     for _ in range(7):
#         print("*********this is fun two************")
#         time.sleep(.5)
# t1=threading.Thread(target=fun1,args=(11,))
# t2=threading.Thread(target=fun2)
# # t1=multiprocessing.Process(target=fun1,args=(15,))
# # t2=multiprocessing.Process(target=fun1)

# t1.start()
# t2.start()
# print("end")
# # fun2()
# t1.join() 
# t2.join()  #join after thread completion
# print("hi")
# print("hi")


#MULTIPROCESS

def fun1(n):
    for _ in range(n):
        print(_,"this is fun one")
        time.sleep(.5)  #wait .5 sec

def fun2():
    for _ in range(7):
        print("*********this is fun two************")
        time.sleep(.5)
# t1=threading.Thread(target=fun1,args=(11,))
# t2=threading.Thread(target=fun2)
if __name__=="__main__":
    t1=multiprocessing.Process(target=fun1,args=(15,))
    t1.start()
    t2=multiprocessing.Process(target=fun2)

    t2.start()
    # fun2()
    t1.join() 
    t2.join()  #join after thread completion
    print("end")
    print("hi")
    print("hi")