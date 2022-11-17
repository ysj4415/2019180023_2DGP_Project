from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import window_size
max_jumppower = 60

class JumpState:
    jumprange = 0
    @staticmethod
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if(event == CC.SPACE_DOWN):
            nom.frame_count = 0
            nom.frame_speed = 30
            JumpState.jumprange = 10
            nom.JUMP_SPEED_KMPH = max_jumppower

        elif(event == CC.SPACE_UP):
            JumpState.jumprange -= 6
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
        if JumpState.jumprange > 0: nom.JUMP_SPEED_KMPH = max_jumppower

        if nom.floor_index == 0:
            if nom.position.translate.x >= window_size.width:
                nom.wall_move('right')
                pass
            elif nom.position.translate.x <= 0:
                nom.wall_move('left')
                pass

        elif nom.floor_index == 1:
            # 벽에 부딪혔는지 체크
            if nom.position.translate.y >= window_size.height:
                nom.wall_move('right')
                pass
            elif nom.position.translate.y <= 0:
                nom.wall_move('left')
                pass
        elif nom.floor_index == 2:
            # 벽에 부딪혔는지 체크
            if nom.position.translate.x >= window_size.width:
                nom.wall_move('left')
                pass
            elif nom.position.translate.x <= 0:
                nom.wall_move('right')
                pass
        elif nom.floor_index == 3:
            # 벽에 부딪혔는지 체크
            if nom.position.translate.y >= window_size.height:
                nom.wall_move('left')
                pass
            elif nom.position.translate.y <= 0:
                nom.wall_move('right')
                pass

    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)

    def handle_collision(nom, other, group):
        mainstate.MainState.handle_collision(nom, other, group)
        if group == 'nom:floors':
            if nom.dir == 0:
                nom.add_event(CC.GOTO_IDLE)
            elif nom.dir != 0:
                nom.add_event(CC.GOTO_MOVE)