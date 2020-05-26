





##         SuperVillain 
##        STRENGTH: 
##      STRETCHES: 
#################:
import threading
from core import gamecontroller
from core import workprogram
from core import keylistener


#def background():
#    workprogram.run( gamecontroller.exerciseEvent )
#def foreground( arx ):
#    keylistener.run( gamecontroller.completionEvent )
#b = threading.Thread( target=background , daemon=True )
#f = threading.Thread( target=foreground , daemon=True , args=(1,) )

b = threading.Thread( 
    target=workprogram.run , 
    daemon=True , 
    args=( gamecontroller.exerciseEvent,) )

f = threading.Thread( 
    target=keylistener.run , 
    daemon=True , 
    args=( gamecontroller.completionEvent,) )

b.start()
f.start()

print('Starting Supervillain..')
gamecontroller.run()