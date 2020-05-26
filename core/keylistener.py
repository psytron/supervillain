import glob
import random
import keyboard
from core import soundx

success_sound_arr =glob.glob("sounds/success/*.wav")
possible_sounds_max_index = len(success_sound_arr)-1
print( success_sound_arr )


def run( callback_in ):	
    def print_pressed_keys(e):
        line = ', '.join( [ str(code) for code in keyboard._pressed_events ] )
        if( line == '71' ):  # NUM LOCK Key =71
            print(' BOOOOM! ') 
            callback_in( {'name':' completion event triggered '} )
            soundx.play( success_sound_arr[ random.randint(0,possible_sounds_max_index ) ])    
    
    
    
    keyboard.hook(print_pressed_keys)
    keyboard.wait()
