

##          SuperVillain 
##         STRENGTH: 
##        STRETCHES: 
###################:
import sys, os
import time, datetime
from os import listdir
import subprocess, random
from datetime import datetime
from os.path import isfile, join
from collections import defaultdict
from colorama import Fore, Back, Style
import subprocess, random
from core import soundx
#from core import workprogram
import threading
import time
import keyboard





def background():
    from core import workprogram
    #print('wow running bg ')
    #while True:
    #    print('whatever')
    #    time.sleep(1)
def foreground():
    # What you want to run in the foreground
    print('wow')

b = threading.Thread( target=background)
f = threading.Thread( target=foreground)
b.start()
f.start()

print(' after the starts ')

total = 0
def print_pressed_keys(e):
    global total
    line = ', '.join( [ str(code) for code in keyboard._pressed_events ] )
    if( line == '51' ): # UPPER RIGHT <
        print(' BOOOOM! ', total)
        total = total +1 
        soundx.play('sounds/success/filterblast.wav')
	
keyboard.hook(print_pressed_keys)
keyboard.wait()
