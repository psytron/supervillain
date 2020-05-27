

import glob, sys, os



###################### CHECK ENV
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS # IN BUNDLE
else:
    bundle_dir = '.'

def getBase():
    return bundle_dir

def getSounds( dirname ):
    base = getBase()
    soundlist = glob.glob(base+"/sounds/"+dirname+"/*.wav")
    return soundlist

def showBundleDir():
    print( '                 : ')
    print( '      bundle_dir : ', bundle_dir )
    print( '     sys.argv[0] : ', sys.argv[0] )
    print( '  sys.executable : ', sys.executable )
    print( '       os.getcwd : ', os.getcwd() )
    print( '                 : ')




    #bundle_dir_alt = sys.argv[0]
    #bundle_dir = os.path.dirname(os.path.abspath(__file__)) # IN PYTHON
    #sound_dir = bundle_dir+'/sounds/'
    #sound_dir = os.path.join( bundle_dir ,'sounds')