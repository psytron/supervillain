



player_score = 0
villain_score = 0 


def showGameState():
    print('    Game is on')
    print('  Player Score: ', player_score )
    print(' Villain Score: ', villain_score )

    if player_score + 5000 < villain_score :
        import sys
        print(' GAME OVER You Lost, You are not the SuperVillain. ')
        sys.exit()


def exerciseEvent( e ):
    global villain_score
    villain_score += 1000
    showGameState()

def completionEvent( e ):
    global player_score
    player_score += 1000
    showGameState()