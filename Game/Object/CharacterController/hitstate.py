from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import game_framework
from Object import Nom
import time

dir = None
char_dir = {'': -1, 'h': 1}

TIMER_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION
class HitState:
    current_time = 0

    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if event == CC.DAMAGE:
            global dir
            # ms.MainState.enter(nom, event)
            dir = nom.dir
            nom.anim_type = 0
            nom.frame_number = 2
            nom.jumppower = 3
            # nom.position.translate.y = 32

            nom.life -= 1
            if nom.life == 0:
                nom.restart()
            nom.frame_count = 0
            nom.frame_speed = 20

            HitState.current_time = time.time()
    @staticmethod
    def exit(nom):
        mainstate.MainState.exit(nom)
        pass

    @staticmethod
    def do(nom):
        # global frame
        # nom.frame = (frame//20) % 2
        # frame += 1

        # nom.frame = (nom.frame + nom.frame_number * ACTION_PER_TIME * game_framework.frame_time) % nom.frame_number
        # nom.image_info[1] = nom.anim_type * nom.image_info[3]

        if time.time() - HitState.current_time > 1:
            if nom.dir == 0: nom.add_event(CC.GOTO_IDLE)
            elif nom.dir != 0: nom.add_event(CC.GOTO_MOVE)
        elif time.time() - HitState.current_time < 0.2:
            nom.move(char_dir[nom.flip])
            nom.JUMP_SPEED_KMPH = 10
        # MainState.do(nom)

    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)