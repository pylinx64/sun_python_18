import pyxel
import random

class App:
    def __init__(self):
        # создает поле для игры
        pyxel.init(160, 160, caption='pyxel-GameV20')
        # запуск игры
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
        
    def draw(self):
        
        pyxel.text(68, 80, '/cyberpank 2088', random.randint(0, 15))
    
App()
