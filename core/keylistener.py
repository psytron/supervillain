

import keyboard

def run( callback_in ):	
    def print_pressed_keys(e):
        line = ', '.join( [ str(code) for code in keyboard._pressed_events ] )
        if( line == '71' ):  # NUM LOCK Key =71
            callback_in( {'name':' completion event triggered '} )
    
    keyboard.hook(print_pressed_keys)
    keyboard.wait()
