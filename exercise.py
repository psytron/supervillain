import sys, os;
import subprocess; import random
import time;    import datetime
from os import listdir
from colorama import Fore, Back, Style
from os.path import isfile, join
from collections import defaultdict
from datetime import datetime


# CHECK ENV
if getattr(sys, 'frozen', False):
    # IN BUNDLE
    bundle_dir = sys._MEIPASS
else:
    # IN PYTHON
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print( '                 : ')
print( '    bundle dir is: ', bundle_dir )
print( '   sys.argv[0] is: ', sys.argv[0] )
print( 'sys.executable is: ', sys.executable )
print( '     os.getcwd is: ', os.getcwd() )

sound_dir = bundle_dir+'/sounds/'

# PLAY SOUND
def playSound( sound_in ):
    sound_path = sound_dir +sound_in
    print(' Playing Sound Path: ',sound_path )
    subprocess.call(["afplay", sound_path])


# VARS 
start_date=datetime.now()
start_time=time.time()
total_points=0
played_hash = defaultdict(int)
mypath='sounds'
sounds_array  =[f for f in listdir(sound_dir) if isfile(join(sound_dir, f))]


# EVENT LOOP 
while True:
    random_delay = random.randint(180,320)
    random_sound = random.randint(0, len(sounds_array)-1)
    curr_sound = sounds_array[random_sound]
    playSound( curr_sound )
    played_hash[ curr_sound ]+=1000
    total_points=total_points+1000
    
    for k,v in played_hash.items():
        print(str(Fore.BLUE)+str(k)+'   '+str(v))
    print( Fore.RED + ' RoboCoach '+' TOTAL POINTS: '+str(total_points),' SINCE: ',start_date )    
    print(Style.RESET_ALL)
    time.sleep(random_delay)
    # HERE IT SHOULD WAIT FOR INPUT OR READ THE BUTTON 
    # TO CONFIRM THE SCORE, OR AT LEASE STOP THE CLOCK 
    # COMMAND LINE ARG SEEMS WAY TO TEDIUMS, SHOULD BE
    # EASY AND FAST. FASTEST WAY TO USB BUTTON FOR MAC and WINDOWS?


#import rumps

#class AwesomeStatusBarApp(rumps.App):
#    @rumps.clicked("Preferences")
#    def prefs(self, _):
#        rumps.alert("jk! no preferences available!")##
#
#    @rumps.clicked("Silly button")
#    def onoff(self, sender):
#        sender.state = not sender.state#
#
#    @rumps.clicked("Say hi")
#    def sayhi(self, _):
#        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")#
#
#if __name__ == "__main__":
#    AwesomeStatusBarApp("Awesome App").run()



