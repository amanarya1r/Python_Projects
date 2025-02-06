import turtle

WIDTH, HEIGHT = 500, 500

screen = turtle.Screen() # Describe screen for turtle modules

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the numer of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("The given input is out of range! Please enter a number between 2 to 10.")
        else:
            print("Please entere a valid input!")

get_number_of_racers()