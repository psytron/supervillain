




#                      __________________
#                     /                 /
#       ___STRENGTH  /     Super       /
#     ___STRETCHES  /    Villain      /
#__________________/________________ /

from threading import Thread
from core import gamecontroller, workprogram, keylistener, taskemitter

k = Thread( target=keylistener.run , daemon=True , args=( gamecontroller.completionEvent,) )
t = Thread( target=taskemitter.run , daemon=True , args=( gamecontroller.taskEvent,) )

k.start()
t.start()
gamecontroller.run()
























#def background():
#    workprogram.run( gamecontroller.exerciseEvent )
#def foreground( arx ):
#    keylistener.run( gamecontroller.completionEvent )
#b = threading.Thread( target=background , daemon=True )
#f = threading.Thread( target=foreground , daemon=True , args=(1,) )
