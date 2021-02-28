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


#while True:

begin_fill()
t.forward(u)
t.left(i)
t.forward(u)
t.left(i)
t.forward(u)
t.left(i)
end_fill()

#-----------------
time.sleep(100)
