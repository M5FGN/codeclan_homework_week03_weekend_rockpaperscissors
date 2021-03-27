from flask import render_template, request, redirect
from play import app
from models.game import *
from models.player import *

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html', title='Instructions')

@app.route('/play')
def playcomputer():
    return render_template('play.html', title='Player 1 vrs The Computer')


# @app.route('/index', methods=['post'])
# def players():
#     player1_name = request.form['player1_name']
#     player1_choice = request.form['player1_choice']
#     player_1 = Player(player1_name, player1_choice)
#     player2_name = request.form['player2_name']
#     player2_choice = request.form['player2_choice']
#     player_2 = Player(player2_name, player2_choice)
#     check_winner(player_1, player_2)
#     return redirect('/results')

@app.route('/rock')
def rock_addplayer2():
    return 'Player 2 add your choice'

@app.route('/paper')
def paper_addplayer2():
    return 'Player 2 add your choice'

@app.route('/scissors')
def scissors_addplayer2():
    return 'Player 2 add your choice'


@app.route('/rock/paper')
def rockpaper():
    return 'Player 2 has won'

@app.route('/rock/scissors')
def rockscissors():
    return 'Player 1 has won'

@app.route('/rock/rock')
def rockrock():
    return 'The game is a draw'

@app.route('/paper/paper')
def paperpaper():
    return 'The game is a draw'

@app.route('/paper/scissors')
def paperscissors():    
    return 'Player 2 has won'

@app.route('/paper/rock')
def paperrock():
    return 'Player 1 has won'

@app.route('/scissors/paper')
def scissorspaper():
    return 'Player 1 has won'

@app.route('/scissors/scissors')
def scissorsscissors():
    return 'The game is a draw'

@app.route('/scissors/rock')
def scissorsrock():
    return 'Player 2 has won'

@app.route('/results')
def results():
    return render_template('results.html', title='Winner', players=players)