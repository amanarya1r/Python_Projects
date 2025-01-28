import random
import os

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

palyers = {}

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
        print(f"{red}{bold}Note:{reset} {underline}{red}{italic}Please enter a 'y' for yes and 'n' for no!{reset}\n")



def start():
    TerminalTop(1)
    while True:
        playerInput = input(f'Number of players: {blue}')
        
        print(reset)

        playerNum = int(playerInput if playerInput.isdigit() else 0)
        
        if playerNum > 1 and playerNum < 7:
            print('you have entered correct number\n')
            return playerNum
        elif playerInput == 'q':
            break
        else:
            print(f'{dim}{red}Please enter a valid input{reset}')

# def NamingPlayer(playerNum):
#     namePlayers = (input(f'Would you like to add player names: {blue}')).tolower()
#     print(reset)
#     for i in playerNum:
#         if namePlayers == 'y':
#             players.player[i].name.append = input(f'player{i}: {cyan}')
#             players.player[i].score.append
#         elif namePlayers == 'n':
#             players.player[i].name.append = player[i]

players = {}

playerNum = 5

def NamingPlayer(playerNum):
    namePlayers = input('Would you like to add player names? (y/n): ').lower()
    
    for i in range(playerNum):
        if i not in players:
            players[i] = {"name": [], "score": []}  # Initialize dictionary structure
        
        if namePlayers == 'y':
            player_name = input(f'Enter name for player {i}: ')
            players[i]["name"].append(player_name)
            players[i]["score"].append(0)
        elif namePlayers == 'n':
            players[i]["name"].append(f'player{i}')
            players[i]["score"].append(0)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


NamingPlayer(playerNum)
print(players)





def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
