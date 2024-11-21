import os
import threading

def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}')

threads = []
for i in range(1000000):
    hello_thread = threading.Thread(target=hello_from_thread)
    hello_thread.start()
    threads.append(hello_thread)

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Running {total_threads} thread(s)')
print(f'The current thrread is {thread_name}')

for t in threads:
    t.join()