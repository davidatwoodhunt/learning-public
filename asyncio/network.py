import time
import requests
import threading

def read_example() -> None:
    response = requests.get('https://www.google.com')
    print(response.status_code)
 
threads = []
for i in range(10000):
    t1 = threading.Thread(target=read_example)
    threads.append(t1)

thread_start = time.time()
_ = [t.start() for t in threads]

print('All running')
_ = [t.join() for t in threads]

thread_end = time.time()
print(f'Running with threads took {thread_end - thread_start:.4f} seconds.')
