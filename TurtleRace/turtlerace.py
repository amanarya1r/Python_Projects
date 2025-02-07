import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'pink', 'blue', 'orange', 'yellow', 'purple', 'black', 'cyan', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the numer of racers (2-10) or 'q' to quit: ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("The given input is out of range! Please enter a number between 2 to 10.")
        elif racers == 'q':
            exit()
        else:
            print("Please entere a valid input!")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color )
        racer.shape('turtle')
        racer.left(90) # it will move the turtle upwards
        racer.penup()
        racer.setpos()
        racer.pendown()
        turtles.append(racer)

def init_turtle():
    screen = turtle.Screen() # Describe screen for turtle modules
    screen.setup(WIDTH, HEIGHT)
    screen.title("🐢Turtle Racing🐢")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS) # it will  shuffle the colors by which it become more randomly placed aroudn the list
colors = COLORS[:racers]

# racer = turtle.Turtle() # it create drawn object on the canvas
create_turtles(colors)