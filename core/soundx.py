
import subprocess

def plajjy( sound_in ):
    sound_path = sound_in
    #subprocess.call(["afplay", sound_path]) # blocks
    subprocess.Popen(["afplay", sound_path]) # non blocks





import os


################# PLAY SOUND
def playSound( sound_in ):
    #sound_path = os.path.join(sound_dir,sound_in)
    #print( ' calling afplay with: ', sound_path )
    #subprocess.call(["afplay", sound_path])    
    pass