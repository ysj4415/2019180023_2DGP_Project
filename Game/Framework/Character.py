from Framework.Pawn import *
from Object.CharacterController.CharacterController import *
import window_size

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index

class character(pawn):
    def __init__(self, x = 0, y = 0, state = None):
        super().__init__(x, y)

        self.dir = 0

        self.jumpradian = 0
        self.jumppower = 65
    def jump(self):

        self.jumpradian = (self.jumpradian + 500 * self.frame_time//1) % 180
        f_index = (self.floor_index + 1) % 4
        jump_range = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index] + y_tuple[f_index])

        if jump_range == 0 :
            if self.dir == 0: self.add_event(END_JUMP_STOP )
            elif self.dir != 0: self.add_event(END_JUMP_MOVE)
            return True
        else: return False

    def move(self, dir):
        self.position.translate.x += self.speed * self.x_tuple[self.floor_index] * dir
        self.position.translate.y += self.speed * self.y_tuple[self.floor_index] * dir
        self.position.translate.x = clamp(self.speed, self.position.translate.x, window_size.width - self.speed)
        self.position.translate.y = clamp(self.speed, self.position.translate.y, window_size.height - self.speed)


