import turtle

# Window
wn = turtle.Screen()
wn.title("Pong Game - InternPe Task 5")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 6
ball.dy = 6

# Score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

# Paddle movement
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor()+20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor()-20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor()+20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor()-20)

# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Game logic
def game_loop():
    global score_a, score_b

    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right border
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier",24,"normal"))

    # Left border
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier",24,"normal"))

    # Paddle B collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor()-50 < ball.ycor() < paddle_b.ycor()+50):
        ball.dx *= -1

    # Paddle A collision
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor()-50 < ball.ycor() < paddle_a.ycor()+50):
        ball.dx *= -1

    wn.ontimer(game_loop, 20)

# Start game
game_loop()

wn.mainloop()