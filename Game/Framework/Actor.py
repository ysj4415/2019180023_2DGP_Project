from pico2d import *
from Framework.Transform import *
import camera
import play_state

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

class actor:
    image = None
    x_tuple = (1, 0, -1, 0)
    y_tuple = (0, 1, 0, -1)
    def __init__(self, x = 0, y = 0, floor_index = 0):
        self.position = transform(x, y)
        self.image_info = None
        self.floor_index = floor_index
        self.flip = ''
        self.frame = 0

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 0,0,0,0

        self.position.rotate = floor_index * 90 / 360 * 2 * math.pi

    def __del__(self):
        pass
    def setfloorindex(self, floor_index):
        self.floor_index = floor_index
        self.position.rotate = floor_index * 90 / 360 * 2 * math.pi
    def loadimage(self, image):
        if actor.image == None: self.image = load_image(image)

    def update(self):
        pass

    def draw(self):
        camera_x1, camera_x2, camera_y1, camera_y2 = camera.get_camera()

        x = self.position.translate.x
        y = self.position.translate.y
        size_x = self.image_info[2] * self.position.scale.x
        size_y = self.image_info[3] * self.position.scale.y
        self.image.clip_composite_draw(int(self.frame) * self.image_info[2], self.image_info[1],
                                        self.image_info[2], self.image_info[3],
                                        self.position.rotate, self.flip,
                                        x - camera_x1, y - camera_y1, size_x, size_y)
        bb = self.get_bb()
        draw_rectangle(bb[0]- camera_x1, bb[1]-camera_y1, bb[2]-camera_x1, bb[3]-camera_y1)
    def get_bb(self):
        if self.floor_index == 0:
            return self.position.translate.x - self.c_left_x, self.position.translate.y - self.c_bottom_y, self.position.translate.x + self.c_right_x, self.position.translate.y + self.c_top_y

        elif self.floor_index == 1:
            return self.position.translate.x - self.c_top_y , self.position.translate.y - self.c_left_x, self.position.translate.x + self.c_bottom_y, self.position.translate.y + self.c_right_x

        elif self.floor_index == 2:
            return self.position.translate.x - self.c_right_x, self.position.translate.y - self.c_top_y, self.position.translate.x + self.c_left_x, self.position.translate.y + self.c_bottom_y

        elif self.floor_index == 3:
            return self.position.translate.x - self.c_bottom_y , self.position.translate.y - self.c_right_x, self.position.translate.x + self.c_top_y, self.position.translate.y + self.c_left_x


        return self.position.translate.x - self.c_left_x, self.position.translate.y - self.c_bottom_y, self.position.translate.x + self.c_right_x, self.position.translate.y + self.c_top_y

    def SetStartTran(self):
        if self.floor_index == 0:
            self.position.translate.x = self.position.translate.x  * PIXEL_PER_METER
            self.position.translate.y = self.position.translate.y  * PIXEL_PER_METER + self.image_info[3] / 2 + 10

        elif self.floor_index == 1:
            self.position.translate.x = play_state.map_size[0] - (self.position.translate.x  * PIXEL_PER_METER + self.image_info[3] / 2 + 10)
            self.position.translate.y = self.position.translate.y  * PIXEL_PER_METER
            pass
        elif self.floor_index == 2:
            self.position.translate.x = play_state.map_size[0] - self.position.translate.x  * PIXEL_PER_METER
            self.position.translate.y = play_state.map_size[1] - (self.position.translate.y  * PIXEL_PER_METER + self.image_info[3] / 2 + 10)
            pass

        elif self.floor_index == 3:
            self.position.translate.x = (self.position.translate.x  * PIXEL_PER_METER + self.image_info[3] / 2 + 10)
            self.position.translate.y = play_state.map_size[1] - (self.position.translate.y  * PIXEL_PER_METER)
            pass

        pass
