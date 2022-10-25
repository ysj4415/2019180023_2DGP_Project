from Framework.Actor import *

class pawn(actor):

    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.frame_number = 0
        self.frame_count = 0
        self.frame_speed = 1

        self.anim_type = 0

    def __del__(self):
        super().__del__()

    def update(self):
        frame = (self.frame_count // self.frame_speed) % self.frame_number
        self.frame_count += 1
        self.image_info[0] = frame * self.image_info[2]
        self.image_info[1] = self.anim_type * self.image_info[3]

