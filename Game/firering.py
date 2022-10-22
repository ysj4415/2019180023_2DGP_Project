from pico2d import *

damagebox = []

ground = 50
frame = None

class FireRing:
    image = None
    def __init__(self, x, y, step):
        self.x = x
        self.y = y

        self.frame = 0
        global frame
        frame = 0

        if step >= 3 or step < 0:
            print("error: step over 3")
        else: self.step = step

        if self.image == None: self.image = load_image('res/character/monster_firering.png')
        self.makeDamageBox()
    def makeDamageBox(self):
        damagebox.append(((self.x - 10, 0), (self.x + 10, 25 * (self.step + 1))))
    def update(self):
        global frame
        self.frame = (frame // 50) % 2
        frame += 1
    def draw(self):
        for i in range(self.step):
            self.image.clip_composite_draw(2 * 60, 0 * 100,
                                           60, 100, 0, '',
                                           self.x,
                                           self.y + 25 * i, 60, 100)
        self.image.clip_composite_draw(self.frame*60, 0 * 100,
                                        60, 100, 0, '',
                                       self.x,
                                       self.y + 25 * self.step, 60, 100)

