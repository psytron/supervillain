
from core import soundx
import glob, random

success_sound_arr =glob.glob("sounds/success/*.wav")
completion_sounds = glob.glob("sounds/success/*.wav")
loss_sounds = glob.glob("sounds/loss/*.wav")
win_sounds = glob.glob("sounds/win/*.wav")

possible_sounds_max_index = len(success_sound_arr)-1
def completion():
    soundx.play( completion_sounds[ random.randint(0,len(completion_sounds)-1 ) ])    

def loss():
    soundx.play( loss_sounds[ random.randint(0,len(loss_sounds)-1 ) ])    

def win():
    soundx.play( win_sounds[ random.randint(0,len(win_sounds)-1 ) ])  

def task( obj ):
    print( obj )
    # inspect obj 
    # play specific sound or ROBO READ 
