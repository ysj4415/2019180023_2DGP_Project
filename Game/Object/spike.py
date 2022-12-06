from pico2d import *
from Framework.Actor import *


ground = 15

class Spike(actor):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 35, 30]
        self.SetStartTran()

        self.loadimage('res/character/trap.png')

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 18,15,18,0
    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass
