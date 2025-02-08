import turtle
import time
import random

WIDTH, HEIGHT = 800, 500
COLORS = ['red', 'green', 'pink', 'blue', 'orange', 'yellow', 'purple', 'black', 'cyan', 'brown', 'grey']

def get_number_of_racers():
    racersx = 0
    while True:
        racersx = input("Enter the numer of racers (2-10) or 'q' to quit: ")
        if racersx.isdigit():
            racersx = int(racersx)
            if 2 <= racersx <= 10:
                return racersx
            else:
                print("The given input is out of range! Please enter a number between 2 to 10.")
        elif racersx == 'q':
            exit()
        else:
            print("Please entere a valid input!")

def race(colors):
    racingTurtle = create_turtles(colors)
    while True:
        for racer in racingTurtle:
            distancex = random.randrange(1,20)
            racer.forward(distancex)
            x, y = racer.pos()
            k = -WIDTH // 2 + 10
            if x <= k:
                return colors[racingTurtle.index(racer)]



def create_turtles(colors):
    turtles = []
    spacingy = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color )
        racer.shape('turtle')
        racer.left(180) # it will move the turtle upwards
        racer.penup() 
        racer.setpos(WIDTH//2 - 40, -HEIGHT//2 + (i + 1) *  spacingy) # for floor division use //
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen() # Describe screen for turtle modules
    screen.setup(WIDTH, HEIGHT)
    screen.title("🐢Turtle Racing🐢")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS) # it will  shuffle the colors by which it become more randomly placed around the list
colors = COLORS[:racers]

# racer = turtle.Turtle() # it create drawn object on the canvas
winner = race(colors)
print(f"The Winner is: {winner}")
time.sleep(5)