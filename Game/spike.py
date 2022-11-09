from pico2d import *
from Framework.Actor import *

damagebox = []

ground = 15

class Spike(actor):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 35, 30]
        self.loadimage('res/character/trap.png')
        self.makeDamageBox()
    def update(self):
        super().update()
    def makeDamageBox(self):
        x = self.position.translate.x
        y = self.position.translate.y
        damagebox.append(((x - 17, y - 15), (x + 17, y)))


