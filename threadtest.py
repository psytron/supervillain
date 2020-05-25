import threading
import time

def background():
    while True:
        print('whatever')
        time.sleep(1)

def foreground():
    # What you want to run in the foreground
    print('wow')

b = threading.Thread( target=background)
f = threading.Thread( target=foreground)

b.start()
f.start()