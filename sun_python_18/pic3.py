import turtle

t=turtle.Pen()
#-------------
t.shape('turtle')
t.forward(100)
#t.write('Hello Киберпанк 2030', align='right', font=('Minecraft Rus Regular', 5))

t.speed(0.5)
colors = ['red', 'cyan', 'brown', 'lime', 'white', 'blue']
for color in range(500):
	t.pencolor(colors[color%6])
	t.left(45)
	t.forward(color)

#-------------
turtle.done()

