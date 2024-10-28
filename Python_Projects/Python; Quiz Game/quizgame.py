print('Welcome to Quiz\n')
playing = input("Do you want to play?(yes or no) \n: ")

#to lower the letters of playing we can use .lower()

if playing != "yes"  :
    quit() #use tab instead of spaces because it can cause some issue

print("\n NOTE: All of your answer has to be in small case. \n")
print("Okay! Let's start playing 😊")

answer = input("What does CPU stand for? ")
if answer == "central processing unit": 
    print("Correct! 🎉\n")
else: 
    print("Incorrect ☹️\n")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit": 
    print("Correct! 🎉\n")
else: 
    print("Incorrect ☹️\n")

answer = input("What does UPS stand for? ")
if answer == "uninterruptible power supply": 
    print("Correct! 🎉\n")
else: 
    print("Incorrect ☹️\n")

answer = input("What does GPS stand for? ")
if answer == "global positioning system": 
    print("Correct! 🎉\n")
else: 
    print("Incorrect ☹️\n")

answer = input("What does APU stand for? ")
if answer == "accelerated processing unit": 
    print("Correct! 🎉\n")
else: 
    print("Incorrect ☹️\n")
    
