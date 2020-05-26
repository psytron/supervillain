#!/usr/bin/python3
import sys, os, subprocess



# CHECK ENV
if getattr(sys, 'frozen', False):
    # IN BUNDLE
    bundle_dir = sys._MEIPASS
else:
    # IN PYTHON
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
print( '                 : ')
print( '    bundle dir is: ', bundle_dir )
print( '   sys.argv[0] is: ', sys.argv[0] )
print( 'sys.executable is: ', sys.executable )
print( '     os.getcwd is: ', os.getcwd() )



# PLAY SOUND
def playSound( sound_in ):
    sound_path = bundle_dir+'/sounds/'+sound_in
    print(' Playing Sound Path: ',sound_path )
    subprocess.call(["afplay", sound_path])

playSound('backburner.wav')
res = os.listdir( bundle_dir )
print( res )
for r in res:
    print( 'R in RES:',r )

res = os.listdir( bundle_dir+'/sounds/' )

for r in res:
    print( r )

#for root, dirs, files in os.walk( bundle_dir ):
#    for filename in files:
#        print(filename)