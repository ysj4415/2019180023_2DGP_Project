from Character.CharacterController import mainstate
from Character.CharacterController import CharacterController as CC

dir = None
frame = None

char_dir = {'': -1, 'h': 1}

class HitState:
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if event == CC.DAMAGE:
            global frame
            global dir
            # ms.MainState.enter(nom, event)
            dir = nom.dir
            nom.anim[0] = 0
            nom.anim[1] = 2
            frame = 0
            nom.jumpradian = 0
            nom.y = 32

            nom.life -= 1
            if nom.life == 0:
                nom.restart()
    def exit(nom):
        mainstate.MainState.exit(nom)
        pass
    def do(nom):
        global frame
        nom.frame = (frame//20) % 2
        frame += 1
        if frame//20 > 2 * 6:
            if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)
        elif frame//20 < 3:
            nom.move(char_dir[nom.flip])
        # MainState.do(nom)

    def draw(nom):
        mainstate.MainState.draw(nom)