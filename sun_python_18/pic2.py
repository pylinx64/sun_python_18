import time
import turtle

t=turtle.Pen()
#----------------
# і - угол, u - размер
i=120
u=200
# меняет форму
t.shape('turtle')
# скорость черепашки
t.speed(0.5)

t.pensize(10)
#while True:
t.color('#05FFEB', '#11FF00')
t.begin_fill()
t.forward(u)
t.left(i)
t.forward(u)
t.left(i)
t.forward(u)
t.left(i)
t.end_fill()

#-----------------
time.sleep(100)
