
import random
import keyboard




def print_pressed_keys(e):
    line = ', '.join( [ str(code) for code in keyboard._pressed_events ] )
    if( line == '71' ):  # NUM LOCK Key =71
        print('yes')
    else:
        print('no')

keyboard.hook(print_pressed_keys)
keyboard.wait()
