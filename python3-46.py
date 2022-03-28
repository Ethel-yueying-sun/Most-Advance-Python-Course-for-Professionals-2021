# Thread Locking
# Avoiding the dreaded conditions and deadlocks
# Race condition: same resource modifed by multiple threads
# Deadlock: multiple threads waiting on the same resource

"""
https://wiki.python.org/moin/GlobalInterpreterLock
https://hackernoon.com/has-the-python-gil-been-slain-9440d28fa93d
"""

# Imports and globals
import logging
import threading
from concurrent.futures import ThreadPoolExecutor, thread
import time
import random

counter = 0

# Test function
def test(count):
    global counter
    threadname = threading.currentThread().name
    logging.info(f'Starting: {threadname}')
    
    for _ in range(count):
        logging.info(f'Count: {threadname} += {count}')

        # The global interpreter lock (GIL) in action
        # counter += 1

        # # Locking
        # lock = threading.Lock()
        # # Think this step is to ask for a key to the door of the resources, and the number of the key is only one, so the second step that ask for the same key won't be succeed ever, and each thread will be stuck in this step that between the '1111111' and the '22222222'
        # lock.acquire()
        # print('1111111')
        # lock.acquire() # deadlock - waiting on resources
        # print('2222222')
        # try:
        #     counter += 1
        # finally:
        #     lock.release()

        # Locking Simplified
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {threadname}')
            counter += 1 
            time.sleep(2)

    logging.info(f'Completed: {threadname}')

# Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for _ in range(workers*2):
            v = random.randrange(1, 5)
            # ThreadPool submits a value(v) to a function(test) 
            ex.submit(test, v)

    print(f'Counter: {counter}')
    logging.info('App Finished')

if __name__ == '__main__':
    main()