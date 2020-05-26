
import sys
import subprocess


############################# CHECK ENV
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS # IN BUNDLE
else:
    #bundle_dir = os.path.dirname(os.path.abspath(__file__)) # IN PYTHON
    bundle_dir = ''
    bundle_dir_alt = sys.argv[0]



def play( sound_in ):
    # This should do magic path finding etc? Just play file? 
    # is that better than passing it around 
    #
    sound_path = sound_in
    subprocess.call(["afplay", sound_path])
