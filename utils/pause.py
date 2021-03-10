import time

def pause(delay):
    t = time.time()
    while True:
        if t + delay <= time.time():
            break
