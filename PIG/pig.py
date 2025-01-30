import random
import os
import re
from pynput import keyboard

# =============================== #
bold = '\033[1m'
italic = '\033[3m'
strike = '\033[9m'
underline = '\033[4m'
dim = '\033[2m'

reset = '\033[0m'

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
cyan = '\033[36m'
# =============================== #

exitFlag = False

players = {}

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for macOS/Linux
    else:
        os.system('clear')

def TerminalTop(x):
    if x == 1:
        print(f"{red}{bold}Note:{reset} {underline}{red}{italic}Please enter a valid number between '2' to '6' or 'q' to quit!{reset}\n")
    elif x == 2:
        print(f"{red}{bold}Note:{reset} {underline}{red}{italic}Please enter or press a 'y' for yes and 'n' for no!{reset}\n")
    elif x == 3:
        clear()
        print(f"{red}{bold}Note:{reset} {underline}{red}{italic}Please enter a name without symbols[!, @, $, ., ,, _, *, etc] and spaces!{reset}\n")
    elif x == 4:
        print(f'{dim}{red}Please enter a valid input{reset}')



def start():
    TerminalTop(1)
    global exitFlag
    exitFlag = True
    while True:
        playerInput = input(f'Number of players: {blue}')
        
        print(reset)

        playerNum = int(playerInput if playerInput.isdigit() else 0)
        
        if playerNum > 1 and playerNum < 7:
            print('you have entered correct number\n')
            exitFlag = False
            return playerNum
        elif playerInput == 'q':
            exit()
        else:
            TerminalTop(4)



def NamingPlayer(playerNum):
    while True:
        TerminalTop(2)
        namePlayers = (input(f'Would you like to add player names: {blue}')).lower()
        print(reset)

        if namePlayers == 'y' or namePlayers == 'n':
            for i in range(playerNum):
                j = i+1
                if namePlayers == 'y':
                    TerminalTop(3)
                    while True:
                        playerName = input(f'player{j}: {cyan}')
                        print(reset)

                        if re.search(r"[^a-zA-Z0-9]", playerName):
                            TerminalTop(4)
                        else:
                            break

                    players[f"player_{playerName}"] = {"name": '', "score": 0}
                    players[f"player_{playerName}"]["name"] = playerName

                elif namePlayers == 'n':
                    players[f"player{j}"] = {"name": '', "score": 0} 
                    players[f"player{j}"]["name"] = (f"player{j}")

            return players
        
        else:
            print(f'{dim}{red}Please enter a valid input{reset}\n')


print(NamingPlayer(start()))



def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
