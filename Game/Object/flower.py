from pico2d import *
from Framework.Pawn import *


ground = 15

class Flower(pawn):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 64, 64]
        self.loadimage('res/character/monster_flower.png')

        self.frame_number = 2
        self.anim_type = 0

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 10,32,10,0
    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass
