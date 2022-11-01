from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import window_size


class JumpState:
    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if(event == CC.SPACE_DOWN):
            nom.frame_count = 0
            nom.frame_speed = 30
            nom.jumppower = 5
        nom.anim_type = 3
        nom.frame_number = 8

    @staticmethod
    def exit(nom):
        mainstate.MainState.exit(nom)
        nom.anim_type = 5
        nom.frame_number = 7

    @staticmethod
    def do(nom):
        mainstate.MainState.do(nom)
        nom.jump()

        if nom.position.translate.y == nom.image_info[3] / 2:
            if nom.dir == 0: nom.add_event(CC.GOTO_IDLE)
            elif nom.dir != 0: nom.add_event(CC.GOTO_MOVE)
        # mainstate.MainState.do(nom)
        #
        # if nom.jump() == True: return 0
        #
        # x = nom.position.translate.x
        # y = nom.position.translate.y
        #
        # dir = ''
        # moveline = x * CC.x_tuple[nom.floor_index % 2] + y * CC.y_tuple[nom.floor_index % 2]
        # moveindex = CC.x_tuple[nom.floor_index] + CC.y_tuple[nom.floor_index]
        # move_winsize = window_size.width * CC.x_tuple[nom.floor_index % 2] + window_size.height * CC.y_tuple[nom.floor_index % 2]
        #
        # if moveline == (0 + nom.speed * moveindex) % move_winsize:
        #     dir = 'left'
        # elif moveline == (0 - nom.speed * moveindex) % move_winsize:
        #     dir = 'right'
        #
        # if(dir != '') :
        #     nom.wall_move(dir)
        #     nom.jumpradian = 0
        #     nom.empty_event_que()
        #     if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
        #     elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)

    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)