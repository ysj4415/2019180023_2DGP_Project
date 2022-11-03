from Object.CharacterController import CharacterController as CC
import math

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index

frame = None

class MainState:
    @staticmethod
    def enter(nom, event):
        if event == CC.RIGHT_DOWN:
            nom.dir+=1
        elif event == CC.LEFT_DOWN:
            nom.dir-=1
        elif event ==  CC.RIGHT_UP:
            nom.dir-=1
        elif event == CC.LEFT_UP:
            nom.dir+=1
        nom.dir = CC.clamp(-1, nom.dir, 1)


    @staticmethod
    def exit(nom):
        pass

    @staticmethod
    def do(nom):
        frame = (nom.frame_count // nom.frame_speed) % nom.frame_number
        nom.frame_count += 1
        nom.image_info[0] = frame * nom.image_info[2]
        nom.image_info[1] = nom.anim_type * nom.image_info[3]

        nom.move(nom.dir)

    @staticmethod
    def draw(nom):
        f_index = (nom.floor_index + 1) % 4
        nom.draw()