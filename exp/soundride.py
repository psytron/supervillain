
from pyo import *
s = Server().boot()
s.start()
sf = SfPlayer("sounds/waxonwaxoff.wav", speed=1, loop=True).out()