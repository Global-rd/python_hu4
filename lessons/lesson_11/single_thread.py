import time

def task1():
    print("Task 1 starting...")
    time.sleep(1)
    print("Task 1 finished...")

def task2():
    print("Task 2 starting...")
    time.sleep(3)
    print("Task 2 finished...")

print("Single threaded solution")
task1()
task2()