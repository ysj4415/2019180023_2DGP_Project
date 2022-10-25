from pico2d import *
from Framework.Transform import *

class actor:
    image = None
    x_tuple = (1, 0, -1, 0)
    y_tuple = (0, 1, 0, -1)
    def __init__(self, x = 0, y = 0, floor_index = 0):
        self.position = transform(x, y)
        self.image_info = None
        self.floor_index = floor_index
        self.flip = ''

        self.position.rotate = floor_index * 90 / 360 * 2 * math.pi

    def __del__(self):
        pass
    def loadimage(self, image):
        if self.image == None: self.image = load_image(image)

    def update(self):
        pass

    def draw(self):
        x = self.position.translate.x
        y = self.position.translate.y
        size_x = self.image_info[2] * self.position.scale.x
        size_y = self.image_info[3] * self.position.scale.y
        self.image.clip_composite_draw(self.image_info[0], self.image_info[1],
                                        self.image_info[2], self.image_info[3],
                                        self.position.rotate, self.flip,
                                        x, y, size_x, size_y)
