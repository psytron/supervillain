




#                      __________________
#                     /                 /
#       ___STRENGTH  /     Super       /
#     ___STRETCHES  /    Villain      /
#__________________/________________ /

from threading import Thread
from core import gamecontroller
from core import workprogram
from core import keylistener

b = Thread( target=workprogram.run , daemon=True , args=( gamecontroller.exerciseEvent,) )
f = Thread( target=keylistener.run , daemon=True , args=( gamecontroller.completionEvent,) )

b.start()
f.start()

gamecontroller.run()


























#def background():
#    workprogram.run( gamecontroller.exerciseEvent )
#def foreground( arx ):
#    keylistener.run( gamecontroller.completionEvent )
#b = threading.Thread( target=background , daemon=True )
#f = threading.Thread( target=foreground , daemon=True , args=(1,) )
