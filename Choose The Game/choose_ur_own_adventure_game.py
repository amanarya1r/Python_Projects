name = input("Type your name\n: ")
print("Welcome", name, "to this adventure game!")

answer = input("This is forest of sagar and filled with exotic species which is very dangerous which path would you like to take left ro right?\n: ").lower()

if answer == "left":
    answer = input("You came ot a river, you can walk around it or swim accross? Type walk to walk around it or swim to swim accross?\n: ")
    
    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge, it's damage, do you want to cross it or head back(cross or back)\n: ")
    if answer == "back":
        print("You reached a temple you can decide to drive forward or stay wherever you are. (drive or stay)\n: ")
        if answer == "drive":
            print("You are chased by a woogie man you die you lose.")
        elif answer == "stay":
            print("Woogie reached you and he takes you. You loose")
        else:
            print("Not a valid option. You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you like to talk to them ('nes' or 'no')\n: ")
        if answer == "yes":
            print("You talk to that person and they give you a rare ruby. You win!")
        elif answer == "no":
            print("You ingore the stranger and they are offended so they didn't give the ruby. You loose!")
    else:
        print("Not a valid option. You lose.")
else: 
    print('Not a valid option. You lose.')


print("Credit goes to ni ck le")
