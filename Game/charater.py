from pico2d import *
import math

ground = 32

LEFT_KEY = False
RIGHT_KEY = False
JUMP_KEY = False

def jumprange(jumpradian, jumppower):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi)

class Charater:
    def __init__(self):
        self.x, self.y = 0, ground
        self.frame = 0
        self.image = load_image('PlayerCharacter.png')
        self.anim = [5, 7]
        self.speed = 7
        self.jumpradian = 0
        self.jumppower = 100
        self.onair = False
        self.flip = '0'
    def jump(self):
        self.jumpradian = (self.jumpradian + 10) % 180
        if self.jumpradian== 0 or self.y < ground:
            self.onair = False
    def update(self):
        if LEFT_KEY == True:
            self.flip = 'h'
            self.anim[0] = 4
            self.anim[1] = 8
            if self.x > 5 :  self.x -= self.speed
        elif RIGHT_KEY == True:
            self.flip = '0'
            self.anim[0] = 4
            self.anim[1] = 8
            if self.x < 795 : self.x += self.speed
        elif LEFT_KEY == False and RIGHT_KEY == False:
            self.anim[0] = 5
            self.anim[1] = 7
        if JUMP_KEY == True:
            if self.onair == False :
                self.onair = True

        if self.onair == True:
            self.anim[0] = 3
            self.anim[1] = 8
            self.jump()


        self.frame = (self.frame + 1) % self.anim[1]

    def draw(self):
        # self.image.clip_draw(self.frame*64, self.anim[0] * 64, 64, 64, self.x, self.y + jumprange(self.jumpradian, self.jumppower))
        self.image.clip_composite_draw(self.frame*64, self.anim[0] * 64,
                                        64, 64, 0, self.flip,
                                       self.x, self.y + jumprange(self.jumpradian, self.jumppower), 64, 64)




