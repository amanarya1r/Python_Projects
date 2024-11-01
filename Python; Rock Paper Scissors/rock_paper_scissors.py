import random

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit. \n: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]: #I have created a list, list is anything that capsulated in square brackets that separated by column
        #if user input is not in the list the condition will true
        continue 

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissor: 2

    computer_pick = options [random_number]
    print("Computer picked", computer_pick + ".") #we are not adding ',' after computer_pick bcz it will automatically add space which we don't need 

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1

print(f"You won {user_wins} times.\n The computer won {computer_wins} times.")
print ("Goodbye!")

