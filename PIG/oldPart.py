def playing(players):
    for player in players:

        while True: 
            name_of_player = players[player]['name']
            print(f"{bold}{magenta}{name_of_player}: {red}{italic}Roll the dice?\t{reset}", end='')
            diceRolled = keyPressed()        

            if diceRolled == 'y':
                diceFace = roll()
                diceAnimation(diceFace)

                print(f"{magenta}You got: {yellow}{bold}{diceFace}{reset}")
                if diceFace == 1:
                    print(f"{red}{bold}Oh no! You got 1\n{italic}Your socre is now zero{reset}\n{bold}{underline}Turn over! {cyan}Shifting to next player...{reset}")
                    players[player]['score'] = 0
                else:
                    players[player]['score'] += diceFace
                    print(f"{underline}Your current score is:{reset} {yellow}{bold}{players[player]['score']}{reset}")
                
                if players[player]['score'] >= 50:
                    print(f"{green}{bold}Congratualtions\n{reset}{cyan}{italic}You won the game!!!{reset}")
                    break

            elif diceRolled == 'n':
                print(f"{blue}{italic}{underline}Okay! {cyan}Shifting to next player...{reset}\n")
                break
            else: 
                TerminalTop(4)