import pyxel
import random

SCREEN_X = 180
SCREEN_Y = 180
MAX_SPEED_BUBBLE = 1.8

class Bubble:
    def __init__(self):
        # цвет
        self.color = random.randint(0, 15)
        
        # хранится радиус
        self.radius = random.uniform(1, 10)
        
        # координаты x, y 
        self.position = (random.uniform(1, SCREEN_X),
                        random.uniform(1, SCREEN_Y))

class App:
    def __init__(self):
        # создает поле для игры
        pyxel.init(SCREEN_X, SCREEN_Y, caption='pyxel-GameV20')
        # запуск игры
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
        
    def draw(self):
        # рисует шарик (x, y, радиус, цвет)
        
        bubble = Bubble()
        pyxel.circ(bubble.position[0], bubble.position[1], bubble.radius, bubble.color)
        #pyxel.text(68, 80, '/cyberpank 2088', random.randint(0, 15))
    
App()

