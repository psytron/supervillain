


import random, time
from core import dirspider

#/// INTERIM CONFIG ///
task_array = [ {'type':'sound','dat':f} for f in dirspider.getSounds('task') ]
task_array = task_array+ [  
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


def run( callback_in ):
    # EVENT LOOP 
    while True:
        random_delay = random.randint(90,180)
        random_sound = random.randint(0, len(task_array)-1)
        obj = task_array[random_sound]
        callback_in( obj )
        time.sleep( random_delay )


















        # HERE IT SHOULD WAIT FOR INPUT OR READ THE BUTTON 
        # TO CONFIRM THE SCORE, OR AT LEASE STOP THE CLOCK 
        # COMMAND LINE ARG SEEMS WAY TO TEDIUMS, SHOULD BE
        # EASY AND FAST. FASTEST WAY TO USB BUTTON FOR MAC 
        # and WINDOWS ?