#turtle is like basic pygame. It's for beginners
import turtle
import winsound #it's for sound in windows
import time

#created a window
wn = turtle.Screen()
wn.title("Pong Game!")
wn.bgcolor("black")#backgroun color
wn.setup(width=800, height=600)#to set width, height
wn.tracer(0)#stops the window from updating. give speed to our game a bit


#score points for each player
score_a = 0
score_b = 0

board = turtle.Turtle()#it's for play again button
board1 = turtle.Turtle()#it's for exit button
# draws a rectangle given top left position of a rectangle. It's for buttons
def draw_rectangle(board, x, y, width, height, size, color):
    board.pencolor(color)
    board.pensize(size)
    board.setheading(0)

    board.up()
    board.goto(x, y)
    board.down()
    # draw top
    board.forward(width)
    # draw right
    board.right(90)
    board.forward(height)
    # draw bottom
    board.right(90)
    board.forward(width)
    # draw left
    board.right(90)
    board.forward(height)
    board.end_fill()

pen = turtle.Turtle()
def click(x, y):
    #if pressed x, y coordinates are inside the play again box, play the game again
    if x > -100 and x < 100 and y > -50 and y < 50:
        wn.onscreenclick(None)#make the buttons inactive otherwise if player clicks the button area, game starts over and over again or quits the game while game resuming
        score_a = 0
        score_b = 0

        pen.clear()
        board.clear()
        board1.clear()
        gameplay(score_a, score_b)
    #if coordinates are inside the menu box, returns to menu
    elif x > -100 and x < 100 and y > -160 and y < -60:
        wn.onscreenclick(None)
        pen.clear()
        board.clear()
        board1.clear()
        menu()

#It's for menu buttons
def click1(x, y):
    if x > -100 and x < 100 and y > -50 and y < 50:
        wn.onscreenclick(None)#make the buttons inactive otherwise if player clicks the button area, game starts over and over again or quits the game while game resuming
        score_a = 0
        score_b = 0
        pen.clear()
        board.clear()
        board1.clear()
        gameplay(score_a, score_b)
    #closes the window
    elif x > -100 and x < 100 and y > -160 and y < -60:
        wn.bye()



#set menu buttons
def menu():

    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.color("white")
    pen.write("Pong Game!", align="center", font=("Courier", 24, "normal"))



    draw_rectangle(board, -100, 50, 200, 100, 5, "#FFFFFF")
    board.ht()
    board.penup()
    board.hideturtle()
    board.goto(-35, -15)
    board.color("white")
    board.write("Play", font=("Courier", 20, "normal"))

    draw_rectangle(board1, -100, -60, 200, 100, 5, "#FFFFFF")
    board1.ht()
    board1.penup()
    board1.hideturtle()
    board1.goto(-35, -125)
    board1.color("white")
    board1.write("Quit", font=("Courier", 20, "normal"))

    wn.onscreenclick(click1, 1)
    wn.listen()
    wn.mainloop()



#main game loop
def gameplay(score_a, score_b):
    a = 0 #it's for controlling movement of paddle a

    # Paddle A
    paddle_A = turtle.Turtle()
    paddle_A.speed(0)  # speed for animation. set the speed max. Otherwise it would be slow
    paddle_A.shape("square")  # made paddle as square
    paddle_A.color("white")  # gave a color
    paddle_A.penup()  # do not draw a line
    paddle_A.goto(-350, 0)  # starting coordination. -350=x, y=0
    # default shape of that square is 20x20
    paddle_A.shapesize(stretch_wid=5, stretch_len=1)  # stretch it 20*5 x 20*1 -----> 100x20

    # Paddle B
    paddle_B = turtle.Turtle()
    paddle_B.speed(0)
    paddle_B.shape("square")
    paddle_B.color("white")
    paddle_B.penup()
    paddle_B.goto(350, 0)  # starting coordination. 350=x, y=0
    paddle_B.shapesize(stretch_wid=5, stretch_len=1)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

    # set ball's movement into 2 parts. X and Y movement
    ball.dx = 7  # it goes 7 pixels in both coordinates
    ball.dy = 7

    # function to move paddles
    def paddle_A_up(a):
        y = paddle_A.ycor()  # we have to know y to move the paddle
        if a == 0:#paddle_A will stop
            paddle_A.sety(y)
        else:#paddle_A will move up
            y += 8  # y moves +8 in every move
            paddle_A.sety(y)

    def paddle_A_down(a):
        y = paddle_A.ycor()  # we have to know y to move the paddle
        if a == 0:#paddle_A will stop
            paddle_A.sety(y)
        else:#paddle_A will move down
            y -= 8  # y moves -8 in every move
            paddle_A.sety(y)

    def paddle_B_up():
        y = paddle_B.ycor()
        y += 20
        paddle_B.sety(y)

    def paddle_B_down():
        y = paddle_B.ycor()
        y -= 20
        paddle_B.sety(y)

    # keyboard binding


    wn.listen()  # listen for keyboard input
    wn.onkeypress(paddle_B_up, 'Up')  # when press up, move paddle up
    wn.onkeypress(paddle_B_down, 'Down')  # when press down, move paddle down



    # Pen (Scoring system)
    pen.speed(0)  # animation speed not the movement speed
    pen.color("white")
    pen.penup()
    pen.hideturtle()  # we do not wanna see this. It's like an arrow to draw a line and did hide it.
    pen.goto(0, 260)
    pen.write("Computer: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    while True:
        #to make ball movement consistent. Otherwise ball gets faster and slower everytime window updated itself
        time.sleep(1/60)

        wn.update()#everytime the loop runs, it updates the screen

        #move the ball
        ball.setx(ball.xcor() + ball.dx)#when the game begin, ball moves 7 pixels left
        ball.sety(ball.ycor() + ball.dy)#7 pixels up


        #border checking. we want to bounce the ball at top and down border. we set height as 600. that means begin from 0, +300 to up, -300 to down
        #it reverses the direction
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


        #set down border
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        #it begin from 0, +400 to right, -400 to left.
        #set right and left borders. That means Computer scored. update the scoreboard
        if ball.xcor() > 390:
            ball.goto(0, 0) #ball moves into 0
            ball.dx *= -1
            score_a += 1
            a = 1
            pen.clear()
            pen.write("Computer: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("applause2.wav", winsound.SND_ASYNC)

        # set left border. That means Player B scored. update the scoreboard
        if ball.xcor() < -390:
            ball.goto(0, 0)  # ball moves into 0
            ball.dx *= -1
            score_b += 1
            a = 0
            pen.clear()
            pen.write("Computer: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            winsound.PlaySound("applause2.wav", winsound.SND_ASYNC)#score sound effect

        #paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
            a = 1 #that means ball goes into paddle_A side. So paddle_A has to move to the ball
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)#it's a sound effect that comes after bouncing from border or paddle

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
            a = 0 #ball goes into paddle_B side. so paddle_A will stop
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        #while ball is not at x = -173, paddle_A will not move. if x < -173, paddle_A will move onto ball. If it can not touch the ball, player scores.
        #if let the paddle move while x > -173, paddle will catch the ball everytime so player can not score
        #or we can let paddle move slower but this time, everytime that the ball bounces from the borders, paddle can not catch the ball.
        #so I think something like that.
        if not ball.xcor() > -173:
            #that means ball goes up, so paddle should go up.
            if ball.ycor() > paddle_A.ycor() and abs(paddle_A.ycor() - ball.ycor()) > 10:
                paddle_A_up(a)
            # that means ball goes down, so paddle should go down.
            elif ball.ycor() < paddle_A.ycor() and abs(paddle_A.ycor() - ball.ycor()) > 10:
                paddle_A_down(a)
        #if ball is not at x <= -173, paddle will not move!
        else:
            paddle_A.sety(paddle_A.ycor())

        #player that scores 3 point, wins!
        if score_a == 3 or score_b == 3:
            winsound.PlaySound("mixkit-arcade-retro-game-over-213.wav", winsound.SND_ASYNC)#it's game over sound effect
            pen.clear()
            wn.bgpic(None)
            paddle_B.reset()
            paddle_A.reset()
            ball.reset()
            if score_a == 3:
                pen.goto(0, 260)
                pen.write("GAME OVER! COMPUTER WINS!", align="center", font=("Courier", 24, "normal"))
            else:
                pen.goto(0, 260)
                pen.write("GAME OVER! PLAYER B WINS!", align="center", font=("Courier", 24, "normal"))

            #asks if player wanna continue or return to menu as buttons
            draw_rectangle(board, -100, 50, 200, 100, 5, "#FFFFFF")
            board.ht()
            board.penup()
            board.hideturtle()
            board.goto(-75, -15)
            board.color("white")
            board.write("Play Again", font=("Courier", 20, "normal"))

            draw_rectangle(board1, -100, -60, 200, 100, 5, "#FFFFFF")
            board1.ht()
            board1.penup()
            board1.hideturtle()
            board1.goto(-90, -125)
            board1.color("white")
            board1.write("Return Menu", font=("Courier", 20, "normal"))

            #for player's click choice
            wn.onscreenclick(click, 1)
            wn.listen()
            wn.mainloop()


menu() #begins the game

