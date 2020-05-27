


import random, sys, os, time, subprocess, glob
from collections import defaultdict
from os.path import isfile, join
from datetime import datetime
from os import listdir
from colorama import Fore, Style


############################# CHECK ENV
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS # IN BUNDLE
else:
    #bundle_dir = os.path.dirname(os.path.abspath(__file__)) # IN PYTHON
    bundle_dir = ''
    bundle_dir_alt = sys.argv[0]


print( '                 : ')
print( '      bundle_dir : ', bundle_dir )
print( '     sys.argv[0] : ', sys.argv[0] )
print( '  sys.executable : ', sys.executable )
print( '       os.getcwd : ', os.getcwd() )
print( '                 : ')
sound_dir = bundle_dir+'/sounds/'
#sound_dir = os.path.join( bundle_dir ,'sounds')


################# PLAY SOUND
def playSound( sound_in ):
    sound_path = os.path.join(sound_dir,sound_in)
    print( ' calling afplay with: ', sound_path )
    subprocess.call(["afplay", sound_path])


############# PREPARE ARRAY OF MEDIA 
total_points=0
mypath='sounds'
start_time=time.time()
start_date=datetime.now()
played_hash = defaultdict(int)
#sounds_array =[ {'type':'sound','dat':f} for f in listdir(sound_dir) if isfile(join(sound_dir, f))]
sounds_array = [ {'type':'sound','dat':f} for f in glob.glob( sound_dir+"/*.wav") ]
possible_sounds_max_index = len( sounds_array )-1


instructions_array = [  
    {'type':'instruct' , 'dat':'Cherrie Pickers.. Do it now. '},
    {'type':'instruct' , 'dat':'Regular Lunges. It looks easy, but you can really feel it.'},
    {'type':'instruct' , 'dat':'Arnold Schwartzenegger. Arnold Shwartzenegger yo. Do it.'},
    {'type':'instruct' , 'dat':'Backbend backwards bridge. Make it happen strength for your back.'},
    {'type':'instruct' , 'dat':'Calf Raises 15. Do 15 Calf Raises.'},
    {'type':'instruct' , 'dat':'Sit-ups. Basic Bitch Sit-ups. Do it. Strong Abs.'},
    {'type':'instruct' , 'dat':'Side Leg Raises. Buns Effect. Iron Buns. '},
    {'type':'instruct' , 'dat':'Leg Raises. Laying down flat raise legs. Do it slowly, super slowly. '},
    {'type':'instruct' , 'dat':'Jumping Jacks. You son of a bitch.  I\'m in. '},
    {'type':'instruct' , 'dat':'Mountain Climbers. Some people call this step through lunges....... Yeeeeeah Fuck Yeah yeah bomb diggity. '},
    {'type':'instruct' , 'dat':'Upper Body Hula Hoops. Rotate upper body spine strength. '},
    {'type':'instruct' , 'dat':'Bobble Head Jumping Jacks '}]
sounds_array = sounds_array + instructions_array

def run( callback_in ):
    global total_points
    # EVENT LOOP 
    while True:
        random_delay = random.randint(15,30)
        random_sound = random.randint(0, len(sounds_array)-1)
        obj = sounds_array[random_sound]
        callback_in( {'name':'exercise challange triggered'} )
        
        if obj['type']=='sound':
            playSound( obj['dat'] )
        else:
            os.system('say '+ obj['dat']  )

        played_hash[ obj['dat'] ] += 1000
        total_points=total_points + 1000    
        for k,v in played_hash.items():
            print(str(Fore.BLUE)+str(k)+'   '+str(v))
        print( Fore.RED + ' RoboCoach '+' TOTAL POINTS: '+str(total_points),' SINCE: ',start_date )    
        print( Style.RESET_ALL )
        time.sleep(random_delay)

















        # HERE IT SHOULD WAIT FOR INPUT OR READ THE BUTTON 
        # TO CONFIRM THE SCORE, OR AT LEASE STOP THE CLOCK 
        # COMMAND LINE ARG SEEMS WAY TO TEDIUMS, SHOULD BE
        # EASY AND FAST. FASTEST WAY TO USB BUTTON FOR MAC 
        # and WINDOWS ?