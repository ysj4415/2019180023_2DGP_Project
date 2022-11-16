from pico2d import *
from Framework.Pawn import *


ground = 50

class FireRing(pawn):
    image = None
    def __init__(self, x, y, step):
        super().__init__(x,y + (step * 25))
        self.image_info = [0, 0, 60, 100]

        self.frame_number = 2
        self.frame_speed = 50
        self.TIMER_PER_ACTION = 0.5
        if step >= 3 or step < 0:
            print("error: step over 3")
        else: self.step = step

        self.loadimage('res/character/monster_firering.png')

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 5,50 + (step * 25),5,-17

    def update(self):
        super().update()
    def draw(self):
        for i in range(self.step):
            self.image.clip_composite_draw(2 * 60, 0 * 100,
                                           60, 100, 0, '',
                                           self.position.translate.x, self.position.translate.y - 25 * (i + 1),
                                           60, 100)
        super().draw()

    def handle_collision(self, other, group):
        pass