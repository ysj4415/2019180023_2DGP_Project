from pico2d import *

damagebox = []

ground = 15

class Spike:
    image = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if self.image == None: self.image = load_image('res/character/trap.png')
        self.makeDamageBox()
    def makeDamageBox(self):
        damagebox.append(((self.x - 17, 0), (self.x + 17, 15)))
    def update(self):
        pass
    def draw(self):

        self.image.clip_composite_draw(0, 0,
                                        35, 30, 0, '',
                                       self.x,
                                       self.y, 35, 30)

