from Object.CharacterController.CharacterController import *
from Framework.Pawn import *
import window_size
from UI import Life
import game_framework



TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION

class nom(pawn):
    def __init__(self, x, y):
        super().__init__(x, y, 0)
        self.image_info = [0, 0, 64, 64]
        self.loadimage('res/character/PlayerCharacter.png')
        self.anim_type = 4
        self.frame_number = 8

        self.rotation_radian = 0 / 360 * 2 * math.pi

        # self. life = 3

    def update(self):
        super().update()
        # self.cur_state.do(self)

    def draw(self):
        x = self.position.translate.x
        y = self.position.translate.y
        size_x = self.image_info[2] * self.position.scale.x
        size_y = self.image_info[3] * self.position.scale.y
        self.image.clip_composite_draw(int(self.frame) * self.image_info[2], self.image_info[1],
                                       self.image_info[2], self.image_info[3],
                                       self.position.rotate, self.flip,
                                       x , y, size_x * 1.5, size_y * 1.5)


