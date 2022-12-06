from Object.CharacterController import CharacterController as CC
import game_framework
from Object import Nom
import window_size
import game_framework

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
        # nom.frame = (nom.frame + nom.frame_number * Nom.ACTION_PER_TIME * game_framework.frame_time) % nom.frame_number
        # nom.image_info[1] = nom.anim_type * nom.image_info[3]

        nom.move(nom.dir)

    @staticmethod
    def draw(nom):
        nom.draw()

    def handle_collision(nom, other, group):
        map_size = game_framework.stack[-1].map_size

        if group == 'nom:trap' or group == 'nom:monster':
            if nom.cur_state != CC.HitState: nom.add_event(CC.DAMAGE)
            nom.sound.play()

        if group == 'nom:floors':
            if nom.floor_index == 0:
                nom.position.translate.y = nom.image_info[3] / 2 + other.image_info[3]
                pass
            elif nom.floor_index == 1:
                nom.position.translate.x = map_size[0] - nom.image_info[3] / 2 - other.image_info[3]
                pass
            elif nom.floor_index == 2:
                nom.position.translate.y = map_size[1] - nom.image_info[3] / 2 - other.image_info[3]
                pass
            elif nom.floor_index == 3:
                nom.position.translate.x = nom.image_info[3] / 2 + other.image_info[3]
                pass
        if group == 'nom:up_floors_step':
            if nom.position.translate.y > other.position.translate.y + 50 + 10:
                nom.JUMP_SPEED_KMPH -= 0
                if nom.floor_index == 0:
                    nom.position.translate.y = nom.image_info[3] / 2 + other.image_info[3] + 10
                    pass

            else:
                if nom.floor_index == 0:
                    nom.JUMP_SPEED_KMPH = 1
                    nom.position.translate.y = other.position.translate.y + other.c_bottom_y - nom.image_info[3] / 2
