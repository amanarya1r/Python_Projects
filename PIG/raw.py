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

def print_dice_face(dots):
    dice_face = f"{blue}┌─────────┐{reset}\n"
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


for i in range(1, 7):
    print_dice_face(i)
    # print("\n")  # Add a newline between faces