import time

def measure_time(fn):
    start = time.time()
    result = fn()
    end = time.time()
    print("Elapsed time: ", end - start)
    return result