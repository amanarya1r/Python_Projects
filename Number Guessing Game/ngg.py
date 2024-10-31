import random #we are importing module name random

strt = 0
upper_range = ""


def nu_check(upper_range):
    global strt
    if upper_range.isdigit():
        upper_range = int(upper_range)  #this convert string into int (it will convert only digit)

        if upper_range <= 0:
            print("Please type a number larger than 0 next time.")
            strt += 1
            starter(strt)
    else: 
        print("Please type a number next time.")
        strt += 1
        starter(strt)
    return upper_range

def starter(strt):
    global upper_range
    if strt == 0:
        upper_range = input("Type a number: ")
        upper_range = nu_check(upper_range)
    else:
        restrt = input("Would like to start again?(type y for yes or n for no)")
        if restrt.lower() == "y":
            upper_range = input("Type a number: ")
            upper_range = nu_check(upper_range)
        else:
            print("Okay Bye!!!")
            quit()
    strt = 0
    return upper_range

   
if strt == 0:
    starter(strt)   

    
# print(random.randrange(start, stop))
nu = random.randrange(0, upper_range) #it will generate random number 1 to 10 but does not include 10, so include 10 you have to use randint
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == nu:
        print("You got it!")
        break #elif stament used just after the if statement this make code look cleaner
    elif user_guess > nu:
        print("You were above the number!")
    else: 
        print("You were below the number!")


print(f"\nYou got it in {guesses} guesses.")

