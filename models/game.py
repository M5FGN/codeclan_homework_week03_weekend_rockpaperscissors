from models.player import *

def check_winner(player1, player2):
    winner = ' '
    if player1.choice == player2.choice:
        winner = 'Draw'
    elif player1.choice == 'rock':
        if player2.choice == 'paper':
            winner = 'player2'
        elif player2.choice == 'scissors':
            winner = 'player1'
    elif player1.choice == 'paper':
        if player2.choice == 'rock':
            winner = 'player1'
        elif player2.choice == 'scissors':
            winner = 'player2'
    elif player1.choice == 'scissors':
        if player2.choice == 'rock':
            winner = 'player2'
        elif player2.choice == 'paper':
            winner = 'player2'
    return winner
