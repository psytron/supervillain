





##         SuperVillain 
##        STRENGTH: 
##      STRETCHES: 
#################:
import threading
from core import gamecontroller


def background():
    from core import workprogram
    workprogram.run( gamecontroller.exerciseEvent )
def foreground():
    from core import keylistener
    keylistener.run( gamecontroller.completionEvent )

b = threading.Thread( target=background)
f = threading.Thread( target=foreground)

b.start()
f.start()
print('Started Supervillain..')

