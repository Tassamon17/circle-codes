import turtle

pen = turtle.Turtle()
turtle.title('Tassamon Window')
pen.pencolor('black')
pen.pensize(5)

pen.fillcolor('teal')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(-200,-100)

pen.pendown()
pen.fillcolor('sky blue')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(200,-100)

pen.pendown()
pen.fillcolor('maroon')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(0,-300)

pen.write('Tassamon', move = True, align = 'center',
          font =('papyrus', 90, 'normal'))

turtle.done()