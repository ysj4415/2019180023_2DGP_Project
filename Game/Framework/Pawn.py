from Framework.Actor import *
import game_framework

class pawn(actor):

    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.frame_number = 0
        self.TIMER_PER_ACTION = 0

        self.anim_type = 0

    def __del__(self):
        super().__del__()

    def update(self):
        # ACTION_PER_TIME = 1.0 / self.TIMER_PER_ACTION
        # self.frame = (self.frame + self.frame_number * ACTION_PER_TIME * game_framework.frame_time) % self.frame_number
        self.image_info[1] = self.anim_type * self.image_info[3]

