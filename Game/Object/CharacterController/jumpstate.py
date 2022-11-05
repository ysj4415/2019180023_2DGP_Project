from Object.CharacterController import mainstate
from Object.CharacterController import CharacterController as CC
import window_size
max_jumppower = 3.8

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
        if JumpState.jumprange > 0: nom.jumppower = max_jumppower
        nom.jump()

        if nom.floor_index == 0:
            if nom.position.translate.y == nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)
            # 벽에 부딪혔는지 체크
            if nom.position.translate.x >= window_size.width - nom.speed:
                nom.wall_move('right')
                pass
            elif nom.position.translate.x <= nom.speed:
                nom.wall_move('left')
                pass

        elif nom.floor_index == 1:
            if nom.position.translate.x == window_size.width - nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

            # 벽에 부딪혔는지 체크
            if nom.position.translate.y >= window_size.height - nom.speed:
                nom.wall_move('right')
                pass
            elif nom.position.translate.y <= nom.speed:
                nom.wall_move('left')
                pass
        elif nom.floor_index == 2:
            if nom.position.translate.y == window_size.height - nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)
            # 벽에 부딪혔는지 체크
            if nom.position.translate.x >= window_size.width - nom.speed:
                nom.wall_move('left')
                pass
            elif nom.position.translate.x <= nom.speed:
                nom.wall_move('right')
                pass
        elif nom.floor_index == 3:
            if nom.position.translate.x == nom.image_info[3] / 2:
                if nom.dir == 0:
                    nom.add_event(CC.GOTO_IDLE)
                elif nom.dir != 0:
                    nom.add_event(CC.GOTO_MOVE)

            # 벽에 부딪혔는지 체크
            if nom.position.translate.y >= window_size.height - nom.speed:
                nom.wall_move('left')
                pass
            elif nom.position.translate.y <= nom.speed:
                nom.wall_move('right')
                pass

    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)