


import random, time
from core import dirspider

#/// INTERIM CONFIG ///
task_array = [ {'type':'sound','dat':f} for f in dirspider.getSounds('task') ]
task_array = task_array+ [  
    {'type':'instruct' , 'dat':'Cherrie Pickers.. Do it now. '},
    {'type':'instruct' , 'dat':'Elastic Spear Diver Forward Bubbles.'},
    {'type':'instruct' , 'dat':'24 Spring Loaded One Leg Power Push-Ups.'},
    {'type':'instruct' , 'dat':'Regular Lunges. 12X.'},
    {'type':'instruct' , 'dat':'Arnold Schwartzenegger 10 seconds.'},
    {'type':'instruct' , 'dat':'Backbend backwards bridge. Variety. '},
    {'type':'instruct' , 'dat':'Calf Raises 15. Do 15.'},
    {'type':'instruct' , 'dat':'Sit-ups. Basic Bitch Sit-ups.'},
    {'type':'instruct' , 'dat':'Side Leg Raises. Easy.'},
    {'type':'instruct' , 'dat':'Leg Raises. Laying down flat raise legs. Do it slowly, super slowly. '},
    {'type':'instruct' , 'dat':'Jumping Jacks.'},
    {'type':'instruct' , 'dat':'Mountain Climbers. Some people call this step through lunges. '},
    {'type':'instruct' , 'dat':'Upper Body Hula Hoops. Rotate upper body spine strength. '},
    {'type':'instruct' , 'dat':'Bobble Head Jumping Jacks '}]


def run( callback_in ):
    # EVENT LOOP 
    while True:
        random_delay = random.randint(190,380)
        random_sound = random.randint(0, len(task_array)-1)
        obj = task_array[random_sound]
        callback_in( obj )
        time.sleep( random_delay )


















        # HERE IT SHOULD WAIT FOR INPUT OR READ THE BUTTON 
        # TO CONFIRM THE SCORE, OR AT LEASE STOP THE CLOCK 
        # COMMAND LINE ARG SEEMS WAY TO TEDIUMS, SHOULD BE
        # EASY AND FAST. FASTEST WAY TO USB BUTTON FOR MAC 
        # and WINDOWS ?