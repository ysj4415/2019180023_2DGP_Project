from pico2d import *
from Framework.Pawn import *
import time

ground = 15

class Flower(pawn):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)
        self.image_info = [0, 0, 64, 64]
        self.loadimage('res/character/monster_flower.png')

        self.SetStartTran()

        self.frame_number = 2
        self.anim_type = 0

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 10,32,10,0
        self.time = time.time()

        self.hide = False
    def update(self):
        super().update()
        if time.time() - self.time >= 1:
            if self.hide == False:
                self.loadimage('res/character/monster_flower_white.png')

                self.hide = True
                self.position.rotate = 180 / 360 * 2 * math.pi
                self.position.translate.y -= 64
                self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 10, 0, 10, 32

                pass
            elif self.hide == True:
                self.loadimage('res/character/monster_flower.png')

                self.hide = False
                self.position.rotate = 0 / 360 * 2 * math.pi
                self.position.translate.y += 64
                self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 10, 32, 10, 0

                pass
            self.time = time.time()


    def handle_collision(self, other, group):
        pass
