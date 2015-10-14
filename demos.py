import pydron
import time


@pydron.functional
def slow(i):
    time.sleep(5)
    return i

@pydron.schedule
def loop_demo():
    total = 0
    for i in range(4):
        total = total + slow(i)
    return total
