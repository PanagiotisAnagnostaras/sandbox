# lambdas
print("lambdas")
## lambda args : expression
d = lambda x, y: x * y
print(d(1, 2))

# threads
print("threads")
import threading

t1 = threading.Thread(target=lambda x: print(x**2), args=(4,))
t1.start()
t1.join()

## threads pass by copy and pass by reference
list_1 = [1,1]
list_2 = [2,2]
t2 = threading.Thread(target= lambda x,y=list_2: print(f"address of x {id(x)} address of y {id(y)}"),  args=(list_1,))
print(f"address of list_1 {id(list_1)} address of list_2 {id(list_2)}")
t2.start()
t2.join()

# lock & time measurement
lock = threading.Lock()
shared_res = 0
runs = 1000000
number_of_threads = 10000
def time_consuming_fun_safe():
    global shared_res
    global lock
    for i in range(runs):
        lock.acquire()
        shared_res+=1
        lock.release()
def time_consuming_fun_unsafe():
    global shared_res
    for i in range(runs):
        shared_res+=1
threads = []
for t in range(number_of_threads):
    threads.append(threading.Thread(target=time_consuming_fun_safe))
import typing
threads: typing.List[threading.Thread]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"shared resource with lock {shared_res}")
shared_res = 0
threads = []
for t in range(number_of_threads):
    threads.append(threading.Thread(target=time_consuming_fun_unsafe))
threads: typing.List[threading.Thread]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"shared resource without lock {shared_res}")