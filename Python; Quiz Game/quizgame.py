print('Welcome to Quiz\n')
playing = input("Do you want to play?(yes or no) \n: ")

#to lower the letters of playing we can use .lower() similar there .upper()

if playing.lower() != "yes"  :
    quit() #use tab instead of spaces because it can cause some issue


print("\nOkay! Let's start playing 😊")
tally = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit": 
    print("Correct! 🎉\n")
    tally += 1
else: 
    print("Incorrect ☹️\n")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print("Correct! 🎉\n")
    tally += 1
else: 
    print("Incorrect ☹️\n")

answer = input("What does UPS stand for? ")
if answer.lower() == "uninterruptible power supply": 
    print("Correct! 🎉\n")
    tally += 1
else: 
    print("Incorrect ☹️\n")

answer = input("What does GPS stand for? ")
if answer.lower() == "global positioning system": 
    print("Correct! 🎉\n")
    tally += 1
else: 
    print("Incorrect ☹️\n")

answer = input("What does APU stand for? ")
if answer.lower() == "accelerated processing unit": 
    print("Correct! 🎉\n")
    tally += 1
else: 
    print("Incorrect ☹️\n")
    

print(f"Youg got {tally} questions correct! And {5 - tally} incorrect. So you are {(tally/5)*100}% correct.")
