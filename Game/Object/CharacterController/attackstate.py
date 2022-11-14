from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import game_framework
from Object import Nom

class AttackState:
    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if event == CC.X_DOWN:
            # mainstate.MainState.enter(nom, event)
            nom.anim_type = 1
            nom.frame_number = 3
            nom.frame_count = 0
        nom.frame_speed = 30

    @staticmethod
    def exit(nom):
        mainstate.MainState.exit(nom)
        pass
    @staticmethod
    def do(nom):
        nom.frame = (nom.frame + nom.frame_number * Nom.ACTION_PER_TIME * game_framework.frame_time) % nom.frame_number
        nom.image_info[1] = nom.anim_type * nom.image_info[3]

        if nom.frame_count // nom.frame_speed > 2:
            if nom.dir == 0: nom.add_event(CC.GOTO_IDLE)
            elif nom.dir != 0: nom.add_event(CC.GOTO_MOVE)

        # MainState.do(nom)
    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)