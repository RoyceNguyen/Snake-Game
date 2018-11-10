


import turtle
import time

delay = 0.1
# Set up the screen

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates

# creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0) #start at mid of screen
head.direction = "up"

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
# main game loop
while True:
    window.update()

    move()
    time.sleep(delay)


window.mainloop()