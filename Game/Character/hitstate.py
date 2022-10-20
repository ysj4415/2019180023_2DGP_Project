from Character import mainstate as ms
from Character import CharacterController as CC

dir = None
frame = None

class HitState:
    def enter(nom, event):
        global frame
        global dir
        ms.MainState.enter(nom, event)
        dir = nom.dir
        nom.anim[0] = 0
        nom.anim[1] = 2
        frame = 0
        nom.jumpradian = 0
        nom.y = 32
    def exit(nom):
        ms.MainState.exit(nom)
        pass
    def do(nom):
        global frame
        nom.frame = (frame//20) % 2
        frame += 1
        if frame//20 > 2 * 6:
            if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)
        elif frame//20 < 3:
            nom.move(dir * -1)
        # MainState.do(nom)

    def draw(nom):
        ms.MainState.draw(nom)