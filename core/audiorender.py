
import sys, os
import subprocess
import glob


################# PLAY SOUND
def playSound( sound_in ):
    sound_path = os.path.join(sound_dir,sound_in)
    print( ' calling afplay with: ', sound_path )
    subprocess.call(["afplay", sound_path])



############################# CHECK ENV
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS # IN BUNDLE
else:
    #bundle_dir = os.path.dirname(os.path.abspath(__file__)) # IN PYTHON
    bundle_dir = '.'
    bundle_dir_alt = sys.argv[0]
#sound_dir = bundle_dir+'/sounds/'
sound_dir = os.path.join( bundle_dir ,'sounds')

def showBundleDir():
    print( '                 : ')
    print( '      bundle_dir : ', bundle_dir )
    print( '     sys.argv[0] : ', sys.argv[0] )
    print( '  sys.executable : ', sys.executable )
    print( '       os.getcwd : ', os.getcwd() )
    print( '                 : ')





def play( sound_in ):
    # This should do magic path finding etc? Just play file? 
    # is that better than passing it around 
    sound_path = sound_in
    subprocess.call(["afplay", sound_path])

def getsoundslist():    
    dir_to_scan = sound_dir+"/*.wav"
    sounds_array = glob.glob( dir_to_scan )
    return sounds_array