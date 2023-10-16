import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

"""
@dev: creating a new process takes a bit more time than a thread
@dev: if we try to run `complex_calculation` & `ask_user` concurrently, we'll get an
      EOF because the input was not given and the calc started
      However, running both complex calcs will work (if multi-core CPU)
Summary:
- when we need to wait for something -> threads
- when we need to run 2+ things at the same time -> multiprocess
"""


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


def multiple_processes():
    process1 = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)

    process1.start()
    process2.start()

    start = time.time()

    process1.join()
    process2.join()

    print(f"2-process total time, {time.time() - start}")


def multi_processes_pool():
    start = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f"2-process total time (pool), {time.time() - start}")


def test():
    # single_thread()
    # multiple_processes()
    multi_processes_pool()


"""
1) multiple_processes

Started calculating...
Started calculating...
complex_calculation, 3.940844774246216
complex_calculation, 3.942923069000244
2-process total time, 4.473669767379761
"""
