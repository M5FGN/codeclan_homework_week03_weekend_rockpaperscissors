from flask import render_template, request, redirect
from play import app
from models.game import check_winner
from models.player import Player


# In browser gameplay

@app.route('/')
def player1():
    return 'Player 1 add your choice'

@app.route('/rock')
def rock_addplayer2():
    return 'Player 2 add your choice'

@app.route('/paper')
def paper_addplayer2():
    return 'Player 2 add your choice'

@app.route('/scissors')
def scissors_addplayer2():
    return 'Player 2 add your choice'

@app.route('/<player1_choice>/<player2_choice>')
def browser_play(player1_choice, player2_choice):
    player1 = Player('Player 1', player1_choice)
    player2 = Player('Player 2', player2_choice)
    winner = check_winner(player1, player2)
    return f'The winner is {winner}'

# FIXME Add the re-direct to the return of browser_play() 
@app.route('/<player1_choice>/<player2_choice>/basic_results')
def browser_play_results(player1_choice, player2_choice):
    player1 = Player('Player 1', player1_choice)
    player2 = Player('Player 2', player2_choice)
    winner = check_winner(player1, player2)
    return render_template('basic_results.html', player1=player1, player2=player2, winner=winner, title='Winners')

# GUI Game Play

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html', title='Instructions')

@app.route('/play')
def playcomputer():
    return render_template('play.html', title='Player 1 vrs The Computer')

# FIXME Get the player-name and choice from the form and add the re-direct.
@app.route('/index', methods=['post'])
def play_game():
    player1_name = request.form['player1_name']
    player1_choice  = request.form['player1_choice']
    player1 = Player(player1_name, player1_choice)
    player2_name = request.form['player2_name']
    player2_choice = request.form['player2_choice']
    player2 = Player(player2_name, player2_choice)
    winner = check_winner(player1, player2)
    return winner
    # return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', title='Winner')

# No Longer needed not that check_winner() has been added 

# @app.route('/rock/paper')
# def rockpaper():
#     return 'Player 2 has won'

# @app.route('/rock/scissors')
# def rockscissors():
#     return 'Player 1 has won'

# @app.route('/rock/rock')
# def rockrock():
#     return 'The game is a draw'

# @app.route('/paper/paper')
# def paperpaper():
#     return 'The game is a draw'

# @app.route('/paper/scissors')
# def paperscissors():    
#     return 'Player 2 has won'

# @app.route('/paper/rock')
# def paperrock():
#     return 'Player 1 has won'

# @app.route('/scissors/paper')
# def scissorspaper():
#     return 'Player 1 has won'

# @app.route('/scissors/scissors')
# def scissorsscissors():
#     return 'The game is a draw'

# @app.route('/scissors/rock')
# def scissorsrock():
#     return 'Player 2 has won'

