from pico2d import *
from Framework.Actor import *
import game_framework
import play_state
import title_state
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

class start_button(actor):
    def __init__(self, x, y):
        super().__init__(x,  y, 0)
        self.image_info = [0, 0, 200, 80]
        self.loadimage('res/UI/start_button.png')
        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 100,40,100,40
        self.size = 0.8

        self.sound = load_wav('res/Glass and Metal Collision.wav')
        self.sound.set_volume(40)
    def update(self):
        pass
    def draw(self):
        # self.image.draw(self.position.translate.x, self.position.translate.y)
        self.image.clip_composite_draw(0, 0,
                                        200, 80,
                                        0, '',
                                        self.position.translate.x, self.position.translate.y, 200 * self.size, 80* self.size)

    def isInBox(self, x, y):
        xl, yb, xr, yt = self.get_bb()
        if xl <= x <= xr and yb <= y <= yt:
            return True
        else: return False

    def Click(self):
        self.sound.play()
        game_framework.change_state(play_state)
        pass


class end_button(actor):
    def __init__(self, x, y):
        super().__init__(x,  y, 0)
        self.image_info = [0, 0, 200, 80]
        self.loadimage('res/UI/end_button.png')
        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 100, 40, 100, 40
        self.size = 0.8
        self.sound = load_wav('res/Glass and Metal Collision.wav')
        self.sound.set_volume(40)


    def update(self):
        pass

    def draw(self):
        # self.image.draw(self.position.translate.x, self.position.translate.y)
        self.image.clip_composite_draw(0, 0,
                                       200, 80,
                                       0, '',
                                       self.position.translate.x, self.position.translate.y, 200 * self.size,
                                       80 * self.size)

    def isInBox(self, x, y):
        xl, yb, xr, yt = self.get_bb()
        if xl <= x <= xr and yb <= y <= yt:
            return True
        else:
            return False

    def Click(self):
        self.sound.play()
        game_framework.quit()
        pass

class continue_button(actor):
    def __init__(self, x, y):
        super().__init__(x,  y, 0)
        self.image_info = [0, 0, 200, 80]
        self.loadimage('res/UI/continue_button.png')
        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 100, 40, 100, 40
        self.size = 0.8
        self.sound = load_wav('res/Glass and Metal Collision.wav')
        self.sound.set_volume(40)


    def update(self):
        pass

    def draw(self):
        # self.image.draw(self.position.translate.x, self.position.translate.y)
        self.image.clip_composite_draw(0, 0,
                                       200, 80,
                                       0, '',
                                       self.position.translate.x, self.position.translate.y, 200 * self.size,
                                       80 * self.size)

    def isInBox(self, x, y):
        xl, yb, xr, yt = self.get_bb()
        if xl <= x <= xr and yb <= y <= yt:
            return True
        else:
            return False

    def Click(self):
        self.sound.play()
        game_framework.pop_state()
        pass

class title_button(actor):
    def __init__(self, x, y):
        super().__init__(x,  y, 0)
        self.image_info = [0, 0, 200, 80]
        self.loadimage('res/UI/title_button.png')
        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 100, 40, 100, 40
        self.size = 0.8
        self.sound = load_wav('res/Glass and Metal Collision.wav')
        self.sound.set_volume(40)


    def update(self):
        pass

    def draw(self):
        # self.image.draw(self.position.translate.x, self.position.translate.y)
        self.image.clip_composite_draw(0, 0,
                                       200, 80,
                                       0, '',
                                       self.position.translate.x, self.position.translate.y, 200 * self.size,
                                       80 * self.size)

    def isInBox(self, x, y):
        xl, yb, xr, yt = self.get_bb()
        if xl <= x <= xr and yb <= y <= yt:
            return True
        else:
            return False

    def Click(self):
        self.sound.play()
        game_framework.pop_state()

        game_framework.change_state(title_state)
        pass