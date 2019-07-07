
import random
import PySimpleGUI as sg

# Global variables that all functions know about.
# DO NOT EDIT THESE GLOBAL VARIABLES
# OR YOUR GAME WILL BREAK.
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""
counter = 0
TIED_SCORE = 0
score={'HUMAN':0,'COMPUTER':0, 'COUNTER':0, 'TIE':0}

#Framework for gui
layout = [[sg.Text('Rock, Paper, Scissors')],
        [sg.Text('Computer Score :', size=(15, 0), font=('Helvetica', 10), text_color='red')],
        [sg.Text('', size=(15, 1), font=('Helvetica', 10), text_color='red', key='COMPUTER')],
        [sg.Text('Player Score :', size=(15, 0), font=('Helvetica', 10), text_color='blue')],
        [sg.Text('', size=(15, 1), font=('Helvetica', 10), text_color='blue', key='HUMAN')],
        [sg.Text('Tied Game    :', size=(15, 0), font=('Helvetica', 10), text_color='green')],
        [sg.Text('', size=(15, 1), font=('Helvetica', 10), text_color='green', key='TIE')],
        [sg.Text('Game Count :', size=(15, 0), font=('Helvetica', 10), text_color='black')],
        [sg.Text('', size=(15, 1), font=('Helvetica', 10), text_color='black', key='COUNT')],
        [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors')],
        [sg.T('')],
        [sg.Quit(button_color=('black', 'orange'))]
        ]
window = sg.Window('Rock,Paper,Scissors', layout, auto_size_text=True)

#Generates computers ranomd choice
def random_computer_choice():
    """Choose randomly for computer."""
    return random.choice(range(3))


def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""

    # GLOBAL VARIABLE LINES.
    global COMPUTER_SCORE
    global HUMAN_SCORE
    global score
    global counter
    global TIED_SCORE

    # based on the given human_choice and computer_choice
    # determine who won and increment their score by 1.
    # if tie, then don't increment anyone's score.

    human_number = human_choice
    computer_number = computer_choice

    if computer_number == human_number + 1 or computer_number + 2 == human_number:
        COMPUTER_SCORE = COMPUTER_SCORE + 1
    elif human_number == computer_number:
       TIED_SCORE = TIED_SCORE + 1
    else:
        HUMAN_SCORE = HUMAN_SCORE + 1
    #scoring and counter changes    
    counter = counter + 1
    score['COUNT'] = counter
    score['COMPUTER'] = COMPUTER_SCORE
    score['HUMAN'] = HUMAN_SCORE
    score['TIE'] = TIED_SCORE
    window.Element('COUNT').Update(score['COUNT'])
    window.Element('COMPUTER').Update(score['COMPUTER'])
    window.Element('HUMAN').Update(score['HUMAN'])
    window.Element('TIE').Update(score['TIE'])

# This code is for the GUI part of the game.
# Handler for mouse click on button.
def player_choice(selection):
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = selection
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


# Main loop that repeats the program unti Quit is pressed
def main():
    while (True):
        # This is the code that reads and updates your window
        event, values = window.Read()
        if event is not None:
            if event == 'Rock':
                player_choice(0)
            elif event == 'Paper':
                player_choice(1)
            elif event == 'Scissors':
                player_choice(2)
            else:
                event == 'Quit'      
                break   
            
    window.Close()   # End program

main()
