import time


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time() * 1000
        retval = func(*args, **kwargs)
        end_ts = time.time() * 1000
        print("Function: %s - elapsed time: %.2f (ms)" % (func.__name__, end_ts - beg_ts))
        return retval

    return wrapper


@time_usage
def test_function(sleep_time):
    time.sleep(sleep_time)


if __name__ == '__main__':
    test_function(5)
