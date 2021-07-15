import random
import os
import colored
from colored import stylize

options = ['rock', 'paper', 'scissors']
score = {
    'victory': 0,
    'loss': 0,
    'draw': 0
}

# print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')

victory = None
while victory == None:
    print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
    player = input('Choose rock, paper or scissor: ').lower().strip()
    bot = random.choice(options)

    if player == 'rock':
        if bot == 'rock': 
            score['draw'] = score['draw'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose rock, so it\'s a draw', colored.fg('45')))
        elif bot == 'scissors':
            score['victory'] = score['victory'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('bot chose scissor, you win!', colored.fg('green')))
        elif bot == 'paper':
            score['loss'] = score['loss'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose paper, you lost!', colored.fg('9')))

    elif player == 'paper':
        if bot == 'rock':
            score['victory'] = score['victory'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose rock, you win!', colored.fg('green')))
        elif bot == 'scissors':
            score['loss'] = score['loss'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('bot chose scissor, you lost!', colored.fg('9')))
        elif bot == 'paper':
            score['draw'] = score['draw'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose paper, it\'s a draw', colored.fg('45')))

    elif player == 'scissor':
        if bot == 'rock':
            score['loss'] = score['loss'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose rock, you lost!', colored.fg('9')))
        elif bot == 'scissors':
            score['draw'] = score['draw'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('bot chose scissor, it\'s a draw', colored.fg('45')))
        elif bot == 'paper':
            score['victory'] = score['victory'] + 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[ Score ] | [ BOT:', score['loss'], '] | [ PLAYER:', score['victory'], ']')
            print(stylize('Bot chose paper, you win!', colored.fg('green')))

    input('Press a [ENTER] to try again')
    os.system('cls' if os.name == 'nt' else 'clear')