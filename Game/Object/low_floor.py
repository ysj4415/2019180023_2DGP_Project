from pico2d import *
from Framework.Actor import *


ground = 15

class Low_Floor(actor):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 132, 10]
        self.loadimage('res/map/floor/low_floor.png')

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 66,5,66,5

    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass
