from pico2d import *

damagebox = [(590,0),(610,60)]

ground = 50
frame = None

class FireRing:
    image = None
    def __init__(self, x, y):
        global frame
        self.x = x
        self.y = y
        self.frame = 0
        frame = 0
        if self.image == None: self.image = load_image('res/character/monster_firering.png')

    def update(self):
        global frame
        self.frame = (frame // 50) % 2
        frame += 1
    def draw(self):
        self.image.clip_composite_draw(self.frame*60, 0 * 100,
                                        60, 100, 0, '',
                                       self.x,
                                       self.y + 25, 60, 100)
        self.image.clip_composite_draw(2*60, 0 * 100,
                                        60, 100, 0, '',
                                       self.x,
                                       self.y, 60, 100)
