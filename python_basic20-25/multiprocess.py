import multiprocessing
import random
from time import sleep

def printtime(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds,"seconds, time is", datetime.utcnow())

if __name__ == '__main__':
    import random
    for s in range(3):
        seconds = random.random()
        pro =multiprocessing.Process(target=printtime, args=(seconds,))
        pro.start()