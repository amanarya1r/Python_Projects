import random
import os
import re
import keyboard
import time

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
yellow = '\033[33m'
magenta = '\033[35m'
# =============================== #

exitFlag = True

players = {}

# Game Logo #

logo = f"""
{bold}{red}██████╗{reset}  {bold}{yellow}██╗{reset}        {bold}{green} ██████╗{reset}  
{bold}{red}██╔══██╗{reset} {bold}{yellow}██║{reset}        {bold}{green}██╔════╝{reset}  
{bold}{red}██████╔╝{reset} {bold}{yellow}██║{reset} {bold}{cyan}█████╗{reset} {bold}{green}██║{reset}   {bold}{green}███╗{reset}  
{bold}{red}██╔═══╝{reset}  {bold}{yellow}██║{reset} {bold}{cyan}╚════╝{reset} {bold}{green}██║{reset}    {bold}{green}██║{reset}  
{bold}{red}██║{reset}      {bold}{yellow}██║{reset}         {bold}{green}╚██████╔╝{reset}  
{bold}{red}╚═╝{reset}      {bold}{yellow}╚═╝{reset}          {bold}{green}╚═════╝{reset}   

🎲 {bold}{magenta}Roll or Bust!{reset} 🎲
"""          
    

def clear(y):
    if y == 1:
        time.sleep(.75)
        # for windows
        if os.name == 'nt':
            os.system('cls')
            print(logo)

        # for macOS/Linux
        else:
            os.system('clear')
            print(logo)
    else:
        # for windows
        if os.name == 'nt':
            os.system('cls')
            print(logo)

        # for macOS/Linux
        else:
            os.system('clear')
            print(logo)



def TerminalTop(x):
    if x == 0:
        clear(0)
        print(f"🤑{cyan}{bold}{italic} Welcome to PI-G ('Play it Greedy') game! {reset}🤑\n")
        print(f"{red}{underline}{bold}Note:{reset} {green}{italic}Press 'q' to quit or any key to continue...{reset}\n")
        keyPressed()
    
    elif x == 1:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a valid number between '2' to '6' or 'q' to quit!{reset}\n")
    
    elif x == 2:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter or press a 'y' for yes and 'n' for no!{reset}\n")
    
    elif x == 3:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a name without symbols[!, @, $, ., ,, _, *, etc] and spaces!{reset}\n")
    
    elif x == 4:
        print(f'{dim}{red}Please enter a valid input{reset}')
    
    elif x == 5:
        clear()
        print(f"{italic}{blue}Exi{magenta}tin{yellow}g... {reset}☹️\n\n  {bold}{cyan}Bye! 👋{reset}")



def keyPressed():
    while True:
        key_event = keyboard.read_event(suppress=True) 
        
        if key_event.event_type == "down": 
            press_key = key_event.name.lower()  
            print(f"{blue}{bold}You pressed: {yellow}{italic}{press_key}{reset}\n")
            if press_key == 'q' and exitFlag == True:
                TerminalTop(5)
                exit()
            elif press_key == 'y':
                return 'y'
            elif press_key == 'n':
                return 'n'
            else:
                return None




def startTerminal():

    TerminalTop(1)
    while True:
        playerInput = input(f'Number of players: {blue}')
        
        print(reset)

        playerNum = int(playerInput if playerInput.isdigit() else 0)
        
        if playerNum > 1 and playerNum < 7:
            print('you have entered correct number\n')
            return playerNum
        elif playerInput == 'q':
            exit()
        else:
            TerminalTop(4)



def NamingPlayer(playerNum):
    global exitFlag
    exitFlag = False
    while True:
        TerminalTop(2)
        print(f'Would you like to add player names: {blue}')
        namePlayers = keyPressed()
        print(reset)

        if namePlayers == 'y' or namePlayers == 'n':
            for i in range(playerNum):
                j = i+1
                if namePlayers == 'y':
                    TerminalTop(3)
                    while True:
                        playerName = input(f'player{j}: {cyan}')
                        print(reset)

                        if not playerName or re.search(r"[^a-zA-Z0-9]", playerName):
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



TerminalTop(0)
print(NamingPlayer(startTerminal()))



def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
