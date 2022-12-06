from pico2d import *
from Framework.Actor import *



class High_Floor(actor):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 132, 136]

        self.SetStartTran()
        self.loadimage('res/map/floor/floor.png')

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 66,68,66,50
    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass
class High_Floor_up(actor):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 132, 136]

        self.SetStartTran()
        self.loadimage('res/map/floor/floor.png')

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 66,-50,66,68
    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass


