


import turtle
import time
import random
delay = 0.1
# Set up the screen

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates

# creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0,0) #start at mid of screen
head.direction = "stop"



# creating fruit
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(0,100)
# creating body
body = []

# Functions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keybinding
window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")
window.onkeypress(right, "d")




# main game loop
while True:
    window.update()

    #check for collision with food
    if head.distance(food) < 20:
        #move food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        #add a body part
        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.shape("circle")
        body_part.color("gray")
        body_part.penup()
        body.append(body_part)

    move()
    time.sleep(delay)


window.mainloop()