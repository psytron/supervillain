
import sys, glob, random
from colorama import Fore, Style
from core import soundx
from core import audiorender


game_on = True
player_score = 0
villain_score = 0


success_sound_arr =glob.glob("sounds/success/*.wav")
possible_sounds_max_index = len(success_sound_arr)-1
def playRandomCompletionSound():
    soundx.play( success_sound_arr[ random.randint(0,possible_sounds_max_index ) ])    



def run():
    while game_on == True:
        pass


def showGameState():
    global game_on
    print('     Game is on: ')
    print( Fore.BLUE,'   Player Score: ', Fore.WHITE, player_score )
    print( Fore.BLUE,'  Villain Score: ', Fore.WHITE, villain_score )
    print( Fore.RESET )

    if player_score + 5000 < villain_score :
        print(' GAME OVER You Lost, You are not the SuperVillain. ')
        game_on = False


def exerciseEvent( e ):
    global villain_score
    villain_score += 1000
    showGameState()

def completionEvent( e ):
    global player_score
    player_score += 1000
    showGameState()
    playRandomCompletionSound()