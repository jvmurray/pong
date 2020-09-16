#this is my pong code
import turtle
window=turtle.Screen()
window.title("Pong by Jessica")
window.bgcolor('pink')
window.setup(width=800, height=600)
window.tracer(0)
#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('blue')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle b
#bonus question use composition to create paddle b with as few lines as possible
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('blue')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(0,0)
ball.dx = .25
ball.dy = .25
#Score
score_a=0
score_b=0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260) 
pen.write(f'Player A: {score_a}  Player B: {score_b}', align="center", font=("Courier", 24, "normal"))
#function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    if y<265:
        paddle_a.sety(y)
    print(f'new position is {y}')
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    if y > -260:
        paddle_a.sety(y)
    print(f'new position is {y}')
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    if y<265:
        paddle_b.sety(y)
    print(f'new position is {y}')
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    if y > -260:
        paddle_b.sety(y)
    print(f'new position is {y}')
#keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')
#main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border checking
    if ball.ycor()>=270 or ball.ycor()<=-270:
        ball.dy=-ball.dy
    if ball.xcor()>390: 
        ball.goto(0,0) 
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align="center", font=("Courier", 24, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0) 
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align="center", font=("Courier", 24, "normal"))
    #Paddle and ball collisions
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() >paddle_b.ycor() -50):
        ball.dx=-ball.dx
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() >paddle_a.ycor() -50):
        ball.dx=-ball.dx
