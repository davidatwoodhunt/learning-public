import time
import threading

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
 
    print(f'fib({number}) is {fib(number)}')
 
 
def fibs_with_threads():
    t1 = threading.Thread(target=print_fib,args=(40,))
    t2 = threading.Thread(target=print_fib,args=(41,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

start_threads = time.time()
 
fibs_with_threads()
 
end_threads = time.time()
 
print(f'Threads took {end_threads - start_threads:.4f} seconds.')