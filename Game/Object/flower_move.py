from pico2d import *
from Object.flower import Flower


ground = 15

class Flower_moving(Flower):
    def __init__(self, x, y, index):
        super().__init__(x, y, index)

    def update(self):
        super().update()


    def handle_collision(self, other, group):
        pass
