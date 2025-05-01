import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with lock:
            temp = counter  # Read the current value
            time.sleep(0.00001)  # Introduce a small delay to force a race condition
            counter = temp + 1  # Increment and write back

threads = []
for _ in range(10):  # Increase the number of threads
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final counter value:", counter)
