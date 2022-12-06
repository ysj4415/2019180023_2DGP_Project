from pico2d import *
from Framework.Pawn import *
import camera

ground = 50

class FireRing(pawn):
    image = None
    def __init__(self, x, y, step, floor_index):
        super().__init__(x, y, floor_index)

        self.image_info = [0, 0, 60, 100]

        self.SetStartTran()
        if floor_index == 0:
            self.position.translate.x = self.position.translate.x
            self.position.translate.y = self.position.translate.y + (step * 25)
        elif floor_index == 1:
            self.position.translate.x = self.position.translate.x - (step * 25)
            self.position.translate.y = self.position.translate.y
        elif floor_index == 2:
            self.position.translate.x = self.position.translate.x
            self.position.translate.y = self.position.translate.y - (step * 25)
        elif floor_index == 3:
            self.position.translate.x = self.position.translate.x + (step * 25)
            self.position.translate.y = self.position.translate.y


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
        camera_x1, camera_x2, camera_y1, camera_y2 = camera.get_camera()

        if self.floor_index == 0:
            for i in range(self.step):
                self.image.clip_composite_draw(2 * 60, 0 * 100,
                                               60, 100, self.position.rotate, '',
                                               self.position.translate.x -camera_x1, self.position.translate.y - camera_y1 - 25 * (i + 1),
                                               60, 100)
        elif self.floor_index == 1:
            for i in range(self.step):
                self.image.clip_composite_draw(2 * 60, 0 * 100,
                                               60, 100, self.position.rotate, '',
                                               self.position.translate.x + 25 * (i + 1) - camera_x1, self.position.translate.y - camera_y1,
                                               60, 100)
        elif self.floor_index == 2:
            for i in range(self.step):
                self.image.clip_composite_draw(2 * 60, 0 * 100,
                                               60, 100, self.position.rotate, '',
                                               self.position.translate.x - camera_x1, self.position.translate.y + 25 * (i + 1) - camera_y1,
                                               60, 100)
        elif self.floor_index == 3:
            for i in range(self.step):
                self.image.clip_composite_draw(2 * 60, 0 * 100,
                                               60, 100, self.position.rotate, '',
                                               self.position.translate.x - 25 * (i + 1) - camera_x1, self.position.translate.y - camera_y1,
                                               60, 100)


        super().draw()

    def handle_collision(self, other, group):
        pass