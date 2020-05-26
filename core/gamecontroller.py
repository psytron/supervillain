
import sys, glob, random, time
from datetime import datetime
from colorama import Fore, Style
from collections import defaultdict
from core import soundx, audiorender, soundboard



game_on = True
player_score = 0
villain_score = 0





def run():
    print('Starting Supervillain..')
    while game_on == True:
        time.sleep(1)
        pass
        
    




def showGameState():
    global game_on
    print('     Game is on: ')
    print( Fore.BLUE,'   Player Score: ', Fore.WHITE, player_score )
    print( Fore.BLUE,'  Villain Score: ', Fore.WHITE, villain_score )
    print( Fore.RESET )

    if player_score + 5000 < villain_score :
        print(' GAME OVER You Lost, You are not the SuperVillain. ')
        soundboard.loss()
        game_on = False
    
    if player_score > villain_score + 5000 :
        print(' You are the SuperVillain. ')
        soundboard.win()
        game_on = False        


def taskEvent( e ):
    global villain_score
    villain_score += 1000
    print( e )
    showGameState()

def completionEvent( e ):
    global player_score
    player_score += 1000
    showGameState()
    soundboard.completion()


start_time=time.time()
start_date=datetime.now()
played_hash = defaultdict(int)


def totalsupdate( obj ):
    played_hash[ obj['dat'] ] += 1000
    for k,v in played_hash.items():
        print(str(Fore.BLUE)+str(k)+'   '+str(v))
    print( Fore.RED + ' RoboCoach '+' TOTAL POINTS: SINCE: ',start_date )    
    print( Style.RESET_ALL )
    #time.sleep(random_delay)