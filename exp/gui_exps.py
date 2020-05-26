

#import rumps
#class AwesomeStatusBarApp(rumps.App):
#    @rumps.clicked("Preferences")
#    def prefs(self, _):
#        rumps.alert("jk! no preferences available!")##
#
#    @rumps.clicked("Silly button")
#    def onoff(self, sender):
#        sender.state = not sender.state#
#
#    @rumps.clicked("Say hi")
#    def sayhi(self, _):
#        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")#
#
#if __name__ == "__main__":
#    AwesomeStatusBarApp("Awesome App").run()


# MAC OS VOICES:
# Play Sound File: 
# afplay /System/Library/Sounds/Funk.aiff
# Speak with Voice 
# say done
# There are more sound effect files in /System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/Sounds/.
# say -v ? (in Yosemite) to get a list of voices installed 
# script to say what you want in every available voice: 
# for i in $(say -v \? | awk '{print $1;}'); do echo $i; say -v $i "Build terminated\!"; done 