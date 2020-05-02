import sys, os;
import subprocess; import random
import time;    import datetime
from os import listdir
from colorama import Fore, Back, Style
from os.path import isfile, join
from collections import defaultdict
from datetime import datetime
import os


#     SuperVillain 
#     STRENGTH: 
#     STRETCHES: 


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
    subprocess.call(["afplay", sound_path])




# PREPARE ARRAY OF SOUNDS AND ROBO INSTRUCTIONS
start_date=datetime.now()
start_time=time.time()
total_points=0
played_hash = defaultdict(int)
mypath='sounds'
sounds_array  =[ {'type':'sound','dat':f} for f in listdir(sound_dir) if isfile(join(sound_dir, f))]
instructions_array = [  
    {'type':'instruct' , 'dat':'Cherrie Pickers.. Do it now. '},
    {'type':'instruct' , 'dat':'Backbend backwards bridge. Make it happen strength for your back.'},
    {'type':'instruct' , 'dat':'Calf Raises 15. Do 15 Calf Raises.'},
    {'type':'instruct' , 'dat':'Sit-ups. Basic Bitch Sit-ups. Do it. Strong Abs.'},
    {'type':'instruct' , 'dat':'Side Leg Raises. Buns Effect. Iron Buns. '},
    {'type':'instruct' , 'dat':'Leg Raises. Laying down flat raise legs. Do it slowly, super slowly. '},
    {'type':'instruct' , 'dat':"Jumping Jacks. You son of a bitch.  I\'m in. "},
    {'type':'instruct' , 'dat':'Mountain Climbers. Some people call this step through lunges....... Yeeeeeah Fuck Yeah yeah bomb diggity. '},
    {'type':'instruct' , 'dat':'Mountain Climbers. Some people call this step through lunges....... Ooh We. '}
]
sounds_array = sounds_array + instructions_array





# EVENT LOOP 
while True:
    random_delay = random.randint(190,300)
    random_sound = random.randint(0, len(sounds_array)-1)
    obj = sounds_array[random_sound]
    
    
    if obj['type']=='sound':
        playSound( obj['dat'] )
    else:
        os.system('say '+ obj['dat']  )


    played_hash[ obj['dat'] ]+=1000
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





# MAC OS VOICES:

# Play Sound File: 
# afplay /System/Library/Sounds/Funk.aiff

# Speak with Voice 
# say done
# There are more sound effect files in /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/.

# say -v ? (in Yosemite) to get a list of voices installed 
# script to say what you want in every available voice: 
# for i in $(say -v \? | awk '{print $1;}'); do echo $i; say -v $i "Build terminated\!"; done 