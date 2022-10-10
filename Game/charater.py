from pico2d import *
import Key_Events

class Charater:
    def __init__(self):
        self.x, self.y = 0, 32
        self.frame = 0
        self.image = load_image('PlayerCharacter.png')
        self.anim = [5, 7]
        self.IsJump = False

    def update(self):
        if Key_Events.LEFT_KEY == True:
            self.image = load_image('PlayerCharacter_reverse.png')
            self.anim[0] = 4
            self.anim[1] = 8
            if self.x > 5 :  self.x -=5
        elif Key_Events.RIGHT_KEY == True:
            self.image = load_image('PlayerCharacter.png')
            self.anim[0] = 4
            self.anim[1] = 8
            if self.x < 795 : self.x +=5
        elif Key_Events.LEFT_KEY == False and Key_Events.RIGHT_KEY == False:
            self.anim[0] = 5
            self.anim[1] = 7
        if Key_Events.JUMP == True and self.y == 32:
            self.IsJump = True


        if self.IsJump == True:
            if Key_Events.JUMP == True and self.y < 80: self.y += 7
            else : self.IsJump = False
            self.anim[0] = 4
            self.frame = 4
            self.anim[1] *= -1
        elif self.y > 32:
            self.y -= 7

            if self.y < 32 : self.y = 32



        if self.anim[1] > 0 : self.frame = (self.frame + 1) % self.anim[1]

    def draw(self):
        self.image.clip_draw(self.frame*64, self.anim[0] * 64, 64, 64, self.x, self.y)



