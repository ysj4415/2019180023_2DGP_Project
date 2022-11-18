from pico2d import *
import window_size
import play_state
import math

# if play_state.nom.floor_index == 0:
#     pass
# elif play_state.nom.floor_index == 1:
#     pass
# elif play_state.nom.floor_index == 2:
#     pass
# elif play_state.nom.floor_index == 3:
#     pass

class  Score():
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class  Life():
    life = 3
    def __init__(self):
        self.image = load_image('res/UI/Life.png')
    def update(self):
        pass
    def draw(self):
        if play_state.nom.floor_index == 0:
            for i in range(Life.life):
                self.image.clip_composite_draw(0, 0, 40, 40,
                                               0, '',
                                               20 + i * 20, window_size.height - 20, 40, 40)
            pass
        elif play_state.nom.floor_index == 1:
            for i in range(Life.life):
                self.image.clip_composite_draw(0, 0, 40, 40,
                                               90 / 360 * 2 * math.pi, '',
                                               20, 20 + i * 20, 40, 40)
            pass
        elif play_state.nom.floor_index == 2:
            for i in range(Life.life):
                self.image.clip_composite_draw(0, 0, 40, 40,
                                               180 / 360 * 2 * math.pi, '',
                                               window_size.width - 20 - i * 20, 20, 40, 40)
            pass
        elif play_state.nom.floor_index == 3:
            for i in range(Life.life):
                self.image.clip_composite_draw(0, 0, 40, 40,
                                               270 / 360 * 2 * math.pi, '',
                                               window_size.width - 20 , window_size.height - 20- i * 20, 40, 40)
            pass

class Ui:
    def __init__(self):
        self.life = Life()
        self.score = Score()
    def update(self):
        self.life.update()
        self.score.update()
    def draw(self):
        self.life.draw()
        self.score.draw()