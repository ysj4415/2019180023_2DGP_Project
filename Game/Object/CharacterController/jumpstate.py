from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import window_size
max_jumppower = 3

class JumpState:
    jumprange = 0
    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if(event == CC.SPACE_DOWN):
            nom.frame_count = 0
            nom.frame_speed = 30
            JumpState.jumprange = 10
            nom.jumppower = max_jumppower
        elif(event == CC.SPACE_UP):
            JumpState.jumprange -= 4
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


        JumpState.jumprange -= 0.1
        if JumpState.jumprange > 0: nom.jumppower = max_jumppower
        nom.jump()

        if nom.floor_index == 0:
            if nom.position.translate.y == nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

        elif nom.floor_index == 1:
            if nom.position.translate.x == window_size.width - nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

        elif nom.floor_index == 2:
            if nom.position.translate.y == window_size.height - nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

        elif nom.floor_index == 3:
            if nom.position.translate.x == nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

        # 벽에 부딪혔는지 체크
        

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