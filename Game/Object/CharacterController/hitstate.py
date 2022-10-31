from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC

dir = None

char_dir = {'': -1, 'h': 1}

class HitState:
    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if event == CC.DAMAGE:
            global dir
            # ms.MainState.enter(nom, event)
            dir = nom.dir
            nom.anim_type = 0
            nom.frame_number = 2
            nom.jumpradian = 0
            nom.position.translate.y = 32

            nom.life -= 1
            if nom.life == 0:
                nom.restart()
            nom.frame_count = 0
            nom.frame_speed = 20
    @staticmethod
    def exit(nom):
        mainstate.MainState.exit(nom)
        pass

    @staticmethod
    def do(nom):
        # global frame
        # nom.frame = (frame//20) % 2
        # frame += 1

        frame = (nom.frame_count // nom.frame_speed) % nom.frame_number
        nom.frame_count += 1
        nom.image_info[0] = frame * nom.image_info[2]
        nom.image_info[1] = nom.anim_type * nom.image_info[3]

        if nom.frame_count // nom.frame_speed > 2 * 6:
            if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)
        elif nom.frame_count // nom.frame_speed < 3:
            nom.move(char_dir[nom.flip])
        # MainState.do(nom)

    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)