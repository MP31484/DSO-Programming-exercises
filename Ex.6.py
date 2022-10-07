'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

Extra:
Lizard, Spock
'''
import random

gameElements=['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
userInput=['rock', 'paper', 'scissors', 'r', 'p', 'sc','spock','lizard','sp','l']

gameOver= False;

outcomes={
    ('Rock', 'Scissors'): 'CRUSHES',
    ('Scissors', 'Paper'): 'CUTS',
    ('Paper', 'Rock') : 'COVERS',
    ('Rock', 'Lizard') : 'CRUSHES',
    ('Lizard','Spock') : 'POISONS',
    ('Spock','Scissors') : 'SMASHES',
    ('Scissors', 'Lizard') : 'DECAPITATES',
    ('Lizard', 'Paper') : 'EATS',
    ('Paper', 'Spock') : 'DISAPROVES',
    ('Spock', 'Rock') : 'VAPORIZES',



}

while not gameOver:
    #user input
    userChoice=""
    while userChoice.lower() not in userInput:
        userChoice= input('Rock, Paper, Scissors, Spock or Lizard? ')
    computerChoice = random.choice(gameElements)
    #game here

    print(f'{userChoice} : {computerChoice}')

    if userChoice==computerChoice:
        outcome=f'{userChoice} v {computerChoice}: Draw'
    elif (computerChoice, userChoice) in outcomes:
        outcome = f'Computer Wins : {computerChoice} {outcomes[computerChoice, userChoice]} {userChoice}'
    elif (userChoice, computerChoice) in outcomes:
        outcome = f'You Win : {userChoice} {outcomes[userChoice, computerChoice]} {computerChoice}'
    else:
        outcome = 'Invalid Choice!'



    print(outcome)
    again= input('Do you want to play again? ')
    if again.lower() == 'n':
        gameOver= True
print('Thanks for playing')


