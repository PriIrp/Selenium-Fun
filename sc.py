import multiprocessing as mp
import time
import datetime
import sys
import signal
import os
import Test

def process(hr, minute):
    while True:
        d = datetime.datetime.now()
        if d.hour == hr and d.minute == minute:
            os.kill(os.getppid(), signal.SIGTERM)
            sys.exit()
        else:
            time.sleep(25)


p = mp.Process(target=process, args=(15, 18))
p.start()

print("Hello World")