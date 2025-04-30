# ======================================== #
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

# More colors (using RGB escape codes)
orange = '\033[38;2;255;165;0m'  
teal = '\033[38;2;0;128;128m'    
peach = '\033[38;2;255;218;185m' 
cream = '\033[38;2;250;240;230m' 
forest_green = '\033[38;2;34;139;34m' 
burgundy = '\033[38;2;128;0;32m'
light_gray = '\033[38;2;200;200;200m' 
dark_gray = '\033[38;2;100;100;100m' 
olive = '\033[38;2;128;128;0m' 

# Background colors (using RGB escape codes)
bg_light_gray = '\033[48;2;200;200;200m' # Light Gray background
bg_orange = '\033[48;2;255;165;0m'  # Orange background
# ======================================== #
import pyttsx3



mlogo = f"""
{bold}{red}    • ▌ ▄ ·. {orange} ▄▄▄· {yellow} ·▄▄▄▄  {green} ▄▄▌  {magenta}▪ {cyan} ▄▄▄▄· 
{red}    ·██ ▐███▪{orange}▐█ ▀█ {yellow} ██▪ ██ {green} ██•  {magenta}██{cyan} ▐█ ▀█▪
{red}    ▐█ ▌▐▌▐█·{orange}▄█▀▀█ {yellow} ▐█· ▐█▌ {green}██▪  {magenta}▐█·{cyan}▐█▀▀█▄
{red}    ██ ██▌▐█▌{orange}▐█ ▪▐▌ {yellow}██. ██ {green} ▐█▌▐▌{magenta}▐█▌{cyan}██▄▪▐█
{red}    ▀▀  █▪▀▀▀{orange} ▀  ▀  {yellow} ▀▀▀▀▀• {green}.▀▀▀{magenta} ▀▀▀{cyan}·▀▀▀▀ {reset}
"""

# Print the colored ASCII logo
print(mlogo)

# def clearScreen(y):
    



def TerminalHead(x):
    if x == 0:
        clearScreen(0)
        print(f"🫨{peach}{bold}{italic} Welcome to PI-G ('Play it Greedy') game! {reset}🫨\n")
        print(f"{red}{underline}{bold}Note:{reset} {green}{italic}Press 'q' to quit or 'r' to know rules or any key to continue...{reset}\n")
        keyPressed()
    
    elif x == 1:
        clearScreen(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a valid number between '2' to '6' or 'q' to quit!{reset}\n")
    
    elif x == 2:
        clearScreen(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please press a 'y' for yes and 'n' for no!{reset}\n")
    
    elif x == 3:
        clearScreen(1)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please enter a name without symbols[!, @, $, ., ,, _, *, etc] and spaces!{reset}\n")
    
    elif x == 4:
        print(f'{dim}{red}Please enter a valid input{reset}')
    
    elif x == 5:
        clearScreen(1)
        print(f"{italic}{blue}Exi{magenta}tin{yellow}g... {reset}☹️\n\n  {bold}{cyan}Bye! 👋{reset}\n")

    elif x == 6:
        for playerx in players:
            print(f"{blue}{players[playerx]['name']}{reset}     ", end='')
    
    elif x == 7:
        clearScreen(0)
        print(f"{red}{underline}{bold}Note:{reset} {red}{italic}Please press a 'y' for yes or 'n' for no or 'q' for quit!{reset}\n")

    elif x == 8:
        print(f"\n{red}{underline}{bold}Note:{reset} {red}{italic}Please press a 'y' for yes or 'n' for no or 'l' for leadership board!{reset}\n")


