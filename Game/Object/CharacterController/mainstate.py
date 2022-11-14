from Object.CharacterController import CharacterController as CC
import game_framework
from Object import Nom


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
        nom.frame = (nom.frame + nom.frame_number * Nom.ACTION_PER_TIME * game_framework.frame_time) % nom.frame_number
        print(nom.frame)
        nom.image_info[1] = nom.anim_type * nom.image_info[3]

        nom.move(nom.dir)

    @staticmethod
    def draw(nom):
        f_index = (nom.floor_index + 1) % 4
        nom.draw()