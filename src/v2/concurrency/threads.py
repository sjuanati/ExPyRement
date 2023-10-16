import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    # blocking operation: the main thread is block waiting for smtg to happen
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")


def complex_calculation():
    start = time.time()
    print("Started calculating...")
    [x**2 for x in range(90000000)]
    print(f"complex_calculation, {time.time() - start}")


def single_thread():
    """run 2 different functions sequentially"""
    start = time.time()
    ask_user()
    complex_calculation()
    print(f"single thread total time, {time.time() - start}")


def multiple_threads():
    """run 2 different functions concurrently (not in parallel)"""

    # pass the functions to the threads, but does not execute it yet
    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=ask_user)

    start = time.time()

    # start the execution of thread1 and thread2. They will run concurrently with the main thread.
    thread1.start()
    thread2.start()

    # tell the main thread to wait for thread1 and thread2 to finish their execution before moving on.
    # This ensures that both threads have completed before the total time is printed.
    thread1.join()
    thread2.join()
    print(f"2-thread total time, {time.time() - start}")


def multiple_threads_same():
    """
    run 2 same functions concurrently: it actually takes double time than sequentially,
    because the CPU constantly switches between the 2 threads
    """
    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=complex_calculation)

    start = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f"2-thread total time, {time.time() - start}")


def multiple_with_pool():
    start = time.time()

    # waits for the pool to finish -> pool.shotdown() not needed
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(ask_user)

    print(f"2-thread total time, {time.time() - start}")


def test():
    single_thread()
    multiple_threads()
    multiple_threads_same()
    multiple_with_pool()
    # @dev: don't kill a thread, otherwise deadlock if another thread is waiting for it


"""
1) single_thread()

Enter your name: sergi
Hello, sergi
ask_user, 2.535274028778076
Started calculating...
complex_calculation, 3.828680992126465
single thread total time, 6.3640360832214355

2) multiple_threads()

Started calculating...
Enter your name: sergi
Hello, sergi
ask_user, 2.7161478996276855
complex_calculation, 3.825718641281128
2-thread total time, 3.825928211212158

3) multiple_threads_same()

Started calculating...
Started calculating...
complex_calculation, 7.038404703140259
complex_calculation, 7.731072664260864
2-thread total time, 7.731229066848755

4) multiple_with_pool()

equivalent to multiple_threads()

"""
