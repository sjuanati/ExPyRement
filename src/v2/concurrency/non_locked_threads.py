import time
import random
import queue

from threading import Thread

"""
Queue: it's like a printer: can receive multiple requests, but can only
process one at a time -> shared resource and a queue to lock access when in use
"""

counter = 0
job_queue = queue.Queue()  # things to be printed out
counter_queue = queue.Queue()  # amounts by which to increase counter


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f"New counter value: {counter}")
    time.sleep(random.random())
    print("----------")


def threads_rekt():
    for x in range(10):
        t = Thread(target=increment_counter)
        time.sleep(random.random())
        t.start()


def increment_manager():
    global counter
    while True:
        increment = (
            counter_queue.get()
        )  # waits until an item is available & then locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        job_queue.put((f"New counter value is {counter}", "---------"))
        time.sleep(random.random())
        counter_queue.task_done()  # unlocks the queue


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())
        job_queue.task_done()


def increment_counter_queue():
    counter_queue.put(1)
    time.sleep(random.random())


def threads_queue():
    # will run continuously as deamons
    Thread(target=increment_manager, daemon=True).start()
    time.sleep(random.random())
    Thread(target=printer_manager, daemon=True).start()
    worker_threads = [Thread(target=increment_counter_queue) for _ in range(10)]
    for thread in worker_threads:
        thread.start()
    for thread in worker_threads:
        thread.join()
    counter_queue.join()
    job_queue.join()

def test():
    # threads_rekt()
    threads_queue()
