def b():
    import turtle
    import time
    import random
    delay = 0.1
    score=0
    wn = turtle.Screen()
    wn.title("Snake Game by incendioz")
    wn.bgcolor('green')
    wn.setup(width=1500, height=900,startx=0,starty=0)
    wn.tracer(0)
    tt=turtle.Turtle()
    tt.pensize(5)
    tt.pu()
    tt.goto(-310,310)
    tt.pd()
    tt.fd(620)
    tt.rt(90)
    tt.fd(620)
    tt.rt(90)
    tt.fd(620)
    tt.rt(90)
    tt.fd(620)
    tt.ht()
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"
    food = turtle.Turtle()
    food.speed(0)
    food.shape("square")
    food.color("red")
    food.penup()
    food.goto(0,100)
    snake = []
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color('black')
    pen.penup()
    pen.hideturtle()
    pen.goto(0,310)
    pen.write('score: 0',align='center',font=('courier',24,'normal'))
    snake = []
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
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")
    while True:
        wn.update()
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in snake:
                segment.goto(1000, 1000)
            snake.clear()
            score = 0
            pen.clear()
            pen.write('score: 0',align='center',font=('courier',24,'normal'))
            delay = 0.1
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            snake.append(new_segment)
            delay -= 0.001
            score += 1
            pen.clear()
            pen.write('score: {}'.format(score),align='center',font=('courier',24,'normal'))
        for index in range(len(snake)-1, 0, -1):
            x = snake[index-1].xcor()
            y = snake[index-1].ycor()
            snake[index].goto(x, y)
        if len(snake) > 0:
            x = head.xcor()
            y = head.ycor()
            snake[0].goto(x,y)
        move()    
        for segment in snake:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                for segment in snake:
                    segment.goto(1000, 1000)
                snake.clear()
                score = 0
                pen.clear()
                pen.write('score: 0',align='center',font=('courier',24,'normal'))
                delay = 0.1
        time.sleep(delay)
    wn.screen.exitonclick()
    wn.mainloop()
b()
