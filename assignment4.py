import threading
import time
import random

# Buffer size
BUFFER_SIZE = 5
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer():
    for i in range(10):
        item = random.randint(1, 100)
        
        empty.acquire()
        mutex.acquire()
        
        buffer.append(item)
        print(f"Produced: {item} | Buffer: {buffer}")
        
        mutex.release()
        full.release()
        
        time.sleep(1)

def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()
        
        item = buffer.pop(0)
        print(f"Consumed: {item} | Buffer: {buffer}")
        
        mutex.release()
        empty.release()
        
        time.sleep(2)

# Create threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()