#import sys
#sys.path.append('..')
import keyboard

total = 0

def print_pressed_keys(e):
    global total
    line = ', '.join( [ str(code) for code in keyboard._pressed_events ] )
    #lll = [ str(code) for code in keyboard._pressed_events ]
    #print( type(line) , line , line=='76' , keyboard._pressed_events  , keyboard._pressed_events.keys() )
    # print( line )
	#'\r' and end='' overwrites the previous line.
	#' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
	#print('\r' + line + ' '*40, end='')

    if( line == '51' ): # UPPER RIGHT <
        print(' BOOOOM! ', total)
        total = total +1 
	
keyboard.hook(print_pressed_keys)
keyboard.wait()