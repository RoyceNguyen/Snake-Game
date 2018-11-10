


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
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0) #start at mid of screen
head.direction = "stop"

# Score
score = 0
high_score = 0

# creating fruit
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
# creating body
body = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
         head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left":
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

    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #hide the body parts
        for bod in body:
            bod.goto(1000,1000)



        #clear the body list
        body.clear()
    # check for collision with food
    if head.distance(food) < 20:
        #move food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        #add a body part
        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.shape("square")
        body_part.color("yellow")
        body_part.penup()
        body.append(body_part)

        #Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.write("Score : {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    # move the last segment first in reverse order
    for i in range(len(body) -1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)
    # move segment 0 to where the head is
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)



    move()

    #check for body collision
    for bod in body:
        if bod.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the body parts
            for bod in body:
                bod.goto(1000, 1000)

            # clear the body list
            body.clear()


    time.sleep(delay)


window.mainloop()