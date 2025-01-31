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
rulesGuide = True

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

# Dice Faces #
def print_dice_face(dots):
    dice_face = f"\n\n{blue}┌─────────┐{reset}\n"
    if dots == 1:
        dice_face += f"{blue}│         │{reset}\n"
        dice_face += f"{blue}│    {red}●    {blue}│{reset}\n"  # Red dot
        dice_face += f"{blue}│         │{reset}\n"

    elif dots == 2:
        dice_face += f"{blue}│  {red}●      {blue}│{reset}\n"
        dice_face += f"{blue}│         │{reset}\n"
        dice_face += f"{blue}│      {red}●  {blue}│{reset}\n"

    elif dots == 3:
        dice_face += f"{blue}│  {red}●      {blue}│{reset}\n"
        dice_face += f"{blue}│    {red}●    {blue}│{reset}\n"
        dice_face += f"{blue}│      {red}●  {blue}│{reset}\n"

    elif dots == 4:
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"
        dice_face += f"{blue}│         {blue}│{reset}\n"
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"

    elif dots == 5:
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"
        dice_face += f"{blue}│    {red}●    {blue}│{reset}\n"
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"

    elif dots == 6:
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"
        dice_face += f"{blue}│  {red}●   {red}●  {blue}│{reset}\n"

    dice_face += f"{blue}└─────────┘{reset}\n"
    print(dice_face)
    

def clear(y):
    if y == 1:
        time.sleep(.75)
        if os.name == 'nt':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)

    else:
        if os.name == 'nt':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)



def TerminalTop(x):
    if x == 0:
        clear(0)
        print(f"🤑{cyan}{bold}{italic} Welcome to PI-G ('Play it Greedy') game! {reset}🤑\n")
        print(f"{red}{underline}{bold}Note:{reset} {green}{italic}Press 'q' to quit or 'r' to know rules or any key to continue...{reset}\n")
        keyPressed()
    
    elif x == 1:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a valid number between '2' to '6' or 'q' to quit!{reset}\n")
    
    elif x == 2:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please press a 'y' for yes and 'n' for no!{reset}\n")
    
    elif x == 3:
        clear(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a name without symbols[!, @, $, ., ,, _, *, etc] and spaces!{reset}\n")
    
    elif x == 4:
        print(f'{dim}{red}Please enter a valid input{reset}')
    
    elif x == 5:
        clear(0)
        print(f"{italic}{blue}Exi{magenta}tin{yellow}g... {reset}☹️\n\n  {bold}{cyan}Bye! 👋{reset}")

    elif x == 6:
        for playerx in players:
            print(f"{blue}{players[playerx]['name']}{reset}     ", end='')
    
    elif x == 7:
        clear(0)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please press a 'y' for yes or 'n' for no or 'q' for quit!{reset}\n")



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
            elif press_key == 'r' and rulesGuide:
                rules()
            else:
                return None
            
        

def rules():
    global rulesGuide
    rulesGuide = False
    clear(1)
    TerminalTop(2)
    print(f"{bold}{underline}{yellow}PI-G (Play it Greedy) is a multiplayer dice game.{reset}")
    print(f"{italic}\nThe whole concept of is that user allow to roll the dice as much as they wanted and there score will only but at a cost of loosing it all if they get '1'.{reset}")
    print(f"{bold}{red}\nRules:{reset}")
    print(f"1. First enter the number of players.")
    print(f"2. Decide whether you guys want to add your name or not.")
    print(f"3. Player get a turn to roll the dice press 'y' for yes or 'n' for no and 'q' for quit.")
    print(f"4. Once player get '1' then the score become zero.")
    print(f"5. If any player get score more than or equal 50 than they won.")
    print(f"6. At any point if you press q while rolling dice the game will be over without any winner.")
    print(f"{green}{italic}\n\nWound like to play now?: ", end='')
    while True:
        start_again = keyPressed()
        if start_again == 'y':
            False
            return startingPoint()
        elif start_again == 'n':
            TerminalTop(5)
            exit()
        else:
            TerminalTop(4)

    


def startTerminal():

    TerminalTop(0)
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
                    TerminalTop(6)
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



def playerBar(name):
    clear(0)
    TerminalTop(7)
    for playery in players:
        if players[playery]['name'] == name:
            print(f"{bold}{underline}{cyan}{name}{reset} = {bold}{underline}{yellow}{players[playery]['score']}{reset}    ", end='')
        else:
            print(f"{blue}{players[playery]['name']}{reset} = {green}{players[playery]['score']}{reset}    ", end='')


def diceAnimation(face, name):
    start_time = time.time()
    duration = 0.75

    while time.time() - start_time < duration:
        playerBar(name)
        dice_face = random.randint(1, 6)
        print_dice_face(dice_face)
        time.sleep(0.15)
    else:
        playerBar(name)
        print_dice_face(face)


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


def playing(players):
    global exitFlag
    exitFlag = True
    player_list = list(players.keys())
    current_player_index = 0

    while True: 
        player = player_list[current_player_index]
        name_of_player = players[player]['name']

        playerBar(name_of_player) #show palyer bar

        while True:
            print(f"\n\n{bold}{magenta}{name_of_player}: {red}{italic}Roll the dice?\t{reset}", end='')
            diceRolled = keyPressed()        

            if diceRolled == 'y':
                diceFace = roll()
                diceAnimation(diceFace, name_of_player)

                print(f"{magenta}You got: {yellow}{bold}{diceFace}{reset}\n")
                if diceFace == 1:
                    print(f"{red}{bold}Oh no! You got 1\n{italic}Your socre is now zero{reset}\n{bold}{underline}Turn over! {cyan}Shifting to next player...{reset}")
                    players[player]['score'] = 0
                    time.sleep(2)
                    break
                else:
                    players[player]['score'] += diceFace
                    print(f"{underline}Your current score is:{reset} {yellow}{bold}{players[player]['score']}{reset}\n")
                
                if players[player]['score'] >= 50:
                    print(f"{green}{bold}🎉🎊 Congratualtions 🎊🎉\n{reset}{cyan}{italic}You won the game!!!{reset}")
                    return

            elif diceRolled == 'n':
                print(f"{blue}{italic}{underline}Okay! {cyan}Shifting to next player...{reset}\n")
                break
            else: 
                TerminalTop(4)

        current_player_index = (current_player_index + 1) % len(player_list)
        



def startingPoint():
    playing(NamingPlayer(startTerminal()))

startingPoint()