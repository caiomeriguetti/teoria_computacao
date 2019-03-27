import time
def print_time(func, params):
    st = time.time()
    result = func(*params)
    end = time.time()

    print end - st, result
