# Simple snake game
import turtle
import time
import random

delay = 0.1

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake body
segments = []

# Score
score = 0
high_score = 0

# Pen (Scoring)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Actions
def write_score(score, high_score):
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def game_reset():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    # Reset the score
    global score
    global high_score
    score = 0
    write_score(score, high_score)

    # Hide the segments (couldn't figure out how to delete them)
    global segments
    for segment in segments:
        segment.goto(1000, 1000)

    segments = []

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

def move_body():
    # Move the body segements in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment of the body to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def add_body():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

def update_score():
    # Increase the score
    global score
    global high_score
    score += 10

    if score > high_score:
        high_score = score
    
    write_score(score, high_score)

# Keyboard bindings
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_up, "w")
window.onkey(go_down, "Down")
window.onkey(go_down, "s")
window.onkey(go_left, "Left")
window.onkey(go_left, "a")
window.onkey(go_right, "Right")
window.onkey(go_right, "d")

write_score(score, high_score)

# Main game loop
while True:
    window.update()

    # Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_reset()

    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            game_reset

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random locaion
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)

        # Add a segment
        add_body()

        # Update the score
        update_score()
        
    move_body()
    move()
    time.sleep(delay)

turtle.mainloop()