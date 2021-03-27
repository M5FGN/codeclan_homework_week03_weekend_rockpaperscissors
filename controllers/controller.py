from flask import render_template
from play import app
from models.game import *
from models.player import *

@app.route('/play')
def index():
    return 'Player 1 add your choice'

@app.route('/play/rock')
def rock_addplayer2():
    return 'Player 2 add your choice'

@app.route('/play/paper')
def paper_addplayer2():
    return 'Player 2 add your choice'

@app.route('/play/scissors')
def scissors_addplayer2():
    return 'Player 2 add your choice'


@app.route('/play/rock/paper')
def rockpaper():
    return 'Player 2 has won'

@app.route('/play/rock/scissors')
def rockscissors():
    return 'Player 1 has won'

@app.route('/play/rock/rock')
def rockrock():
    return 'The game is a draw'

@app.route('/play/paper/paper')
def paperpaper():
    return 'The game is a draw'

@app.route('/play/paper/scissors')
def paperscissors():    
    return 'Player 2 has won'

@app.route('/play/paper/rock')
def paperrock():
    return 'Player 1 has won'

@app.route('/play/scissors/paper')
def scissorspaper():
    return 'Player 1 has won'

@app.route('/play/scissors/scissors')
def scissorsscissors():
    return 'The game is a draw'

@app.route('/play/scissors/rock')
def scissorsrock():
    return 'Player 2 has won'
