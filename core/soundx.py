
import subprocess

def play( sound_in ):
    sound_path = sound_in
    subprocess.call(["afplay", sound_path])