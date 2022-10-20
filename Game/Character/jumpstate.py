from Character import mainstate as ms
from Character import CharacterController as CC
import window_size

frame = None

class JumpState:
    def enter(nom, event):
        ms.MainState.enter(nom, event)
        global frame

        nom.anim[0] = 3
        nom.anim[1] = 8

        frame = 0
    def exit(nom):
        ms.MainState.exit(nom)
        nom.anim[0] = 5
        nom.anim[1] = 7
    def do(nom):
        global frame
        ms.MainState.do(nom)
        frame += 2

        if nom.jump() == True: return 0

        dir = ''
        moveline = nom.x * CC.x_tuple[nom.floor_index % 2] + nom.y * CC.y_tuple[nom.floor_index % 2]
        moveindex = CC.x_tuple[nom.floor_index] + CC.y_tuple[nom.floor_index]
        move_winsize = window_size.width * CC.x_tuple[nom.floor_index % 2] + window_size.height * CC.y_tuple[nom.floor_index % 2]

        if moveline == (0 + nom.speed * moveindex) % move_winsize:
            dir = 'left'
        elif moveline == (0 - nom.speed * moveindex) % move_winsize:
            dir = 'right'

        if(dir != '') :
            nom.wall_move(dir)
            nom.jumpradian = 0
            nom.empty_event_que()
            if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)
    def draw(nom):
        ms.MainState.draw(nom)