import multiprocessing
import os
 
 
def hello_from_process():
    print(f'Hello from child process {os.getpid()}!')
if __name__ == '__main__':
    procs= []
    for i in range(1000):
        hello_process = multiprocessing.Process(target=hello_from_process)
        hello_process.start()
        procs.append(hello_process)
 
    print(f'Hello from parent process {os.getpid()}')
 
    _= [h.join() for h in procs]