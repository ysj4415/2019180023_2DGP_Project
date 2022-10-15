from pico2d import *
import window_size
import math

x_tuple = (1,0,-1,0)
y_tuple = (0,1,0,-1)

ground = 32

LEFT_KEY = False
RIGHT_KEY = False
JUMP_KEY = False

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index



class Charater:
    def __init__(self):
        self.x, self.y = window_size.width / 2, ground
        self.frame = 0
        self.image = load_image('PlayerCharacter.png')
        self.anim = [5, 7]
        self.speed = 7
        self.jumpradian = 0
        self.jumppower = 100
        self.rotation_radian = 0 / 360 * 2 * math.pi
        self.onair = False
        self.flip = ''
        self.floor_index = 0

    def jump(self):
        self.jumpradian = (self.jumpradian + 10) % 180

        f_index = (self.floor_index + 1) % 4
        jump_range = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index] + y_tuple[f_index])

        if jump_range == 0 :
            self.onair = False


    def wall_move(self, direction):
        f_index = (self.floor_index + 1) % 4


        if(direction == 'left'):
            self.rotation_radian -= 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index - 1) % 4

        if(direction == 'right'):
            self.rotation_radian += 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index + 1) % 4




        jump = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index])
        self.x = (self.x + jump) * x_tuple[(self.floor_index) % 2]
        jump = jumprange(self.jumpradian, self.jumppower, y_tuple[f_index])
        self.y = (self.y + jump) * y_tuple[(self.floor_index) % 2]

        self.x = (self.x + (ground * x_tuple[(self.floor_index + 1) % 4])) % window_size.width
        self.y = (self.y + (ground * y_tuple[(self.floor_index + 1) % 4])) % window_size.height



    def move(self, dir):
        if self.speed <= self.x <= window_size.width - self.speed and self.speed <= self.y <= window_size.height - self.speed:
            self.x += self.speed * x_tuple[self.floor_index] * dir
            self.y += self.speed * y_tuple[self.floor_index] * dir
        if self.x < self.speed : self.x = self.speed
        elif self.x > window_size.width - self.speed: self.x = window_size.width - self.speed
        elif self.y < self.speed : self.y = self.speed
        elif self.y > window_size.height - self.speed: self.y = window_size.height - self.speed
    def update(self):
        if LEFT_KEY == True:
            self.flip = 'h'
            self.anim[0] = 4
            self.anim[1] = 8
            self.move(-1)
        elif RIGHT_KEY == True:
            self.flip = ''
            self.anim[0] = 4
            self.anim[1] = 8
            self.move(1)
        elif LEFT_KEY == False and RIGHT_KEY == False:
            self.anim[0] = 5
            self.anim[1] = 7
        if JUMP_KEY == True and self.onair == False:
            self.onair = True

        if self.onair == True:
            self.anim[0] = 3
            self.anim[1] = 8
            self.jump()

            dir = ''
            moveline = self.x * x_tuple[self.floor_index % 2] + self.y * y_tuple[self.floor_index % 2]
            moveindex = x_tuple[self.floor_index] + y_tuple[self.floor_index]
            move_winsize = window_size.width * x_tuple[self.floor_index % 2] + window_size.height * y_tuple[self.floor_index % 2]

            if moveline == (0 + self.speed * moveindex) % move_winsize:
                dir = 'left'
            elif moveline == (0 - self.speed * moveindex) % move_winsize:
                dir = 'right'

            if(dir != '') :
                self.wall_move(dir)
                self.onair = False
                self.jumpradian = 0

        self.frame = (self.frame + 1) % self.anim[1]


    def draw(self):
        f_index = (self.floor_index + 1) % 4
        # self.image.clip_draw(self.frame*64, self.anim[0] * 64, 64, 64, self.x, self.y + jumprange(self.jumpradian, self.jumppower))
        self.image.clip_composite_draw(self.frame*64, self.anim[0] * 64,
                                        64, 64, self.rotation_radian, self.flip,
                                       self.x + jumprange(self.jumpradian, self.jumppower, x_tuple[f_index]),
                                       self.y + jumprange(self.jumpradian, self.jumppower, y_tuple[f_index]), 64, 64)




