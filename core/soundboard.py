


from core import soundx
import glob, random
import sys, os
import subprocess
from core import dirspider


base = dirspider.getBase()
completion_sounds = dirspider.getSounds('completion') 
loss_sounds = dirspider.getSounds('loss') 
win_sounds = dirspider.getSounds('win') 



def play( sound_in ):
    print( 'Playing: ',sound_in )
    subprocess.Popen(["afplay", sound_in]) # non blocks


def completion():
    play( completion_sounds[ random.randint(0,len(completion_sounds)-1 ) ])    

def loss():
    play( loss_sounds[ random.randint(0,len(loss_sounds)-1 ) ])    

def win():
    play( win_sounds[ random.randint(0,len(win_sounds)-1 ) ])  

def task( obj ):
    if obj['type']=='sound':
        play( obj['dat'] )
    else:
        os.system('say '+ obj['dat']  )







