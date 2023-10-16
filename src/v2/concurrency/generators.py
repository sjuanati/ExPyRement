"""
basic example of cooperative multitasking using Python's generators.
Each generator/task gets a chance to run (yield a value) in turns,
simulating multiple tasks running concurrently without using threads or processes.
"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1


def gen():
    """
    simulate multitasking without doing threads
    tasks are executed in a round-robin fashion
    """
    tasks = [countdown(10), countdown(5), countdown(20)]

    while tasks:  # while list not empty
        task = tasks[0]
        tasks.remove(task)
        try:
            x = next(task)
            print(x)
            tasks.append(
                task
            )  # Puts the task back to the end of the list so it can continue in the next round
        except StopIteration:  # Raised when the generator has no more items to yield
            print("Task finished")


def test():
    gen()
