from datetime import datetime, timezone, timedelta
import time
import timeit


def f_datetime():
    """datetime & timezone examples"""
    # now in UTC
    today = datetime.now(timezone.utc)
    print(today)

    # tomorrow in UTC
    tomorrow = today + timedelta(days=1)
    print(tomorrow)

    # yesterday in UTC
    yesterday = today - timedelta(days=1)
    print(yesterday)

    # string format
    print(today.strftime("%d-%m-%Y %H:%M:%S"))  # string format time

    # parse format
    user_date = input("Enter the date in YYYY-mm-dd format: ")
    user_date = datetime.strptime(user_date, "%Y-%m-%d")  # string parse time
    print(user_date)


def powers(limit):
    return [x**2 for x in range(limit)]


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(start, end, end - start)


def test():
    f_datetime()

    # measure time - option 1
    start = time.time()
    powers(50000000)
    end = time.time()
    print(start, end, end - start)

    # measure time - option 2 (lambda is used to pass arguments)
    measure_runtime(lambda: powers(50000000))

    # measure specific statements
    print(timeit.timeit("[x**2 for x in range(10)]"))
    print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
