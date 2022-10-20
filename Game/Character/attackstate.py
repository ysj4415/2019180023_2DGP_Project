from Character import mainstate
from Character import CharacterController as CC

frame = None

class AttackState:
    def enter(nom, event):
        global frame
        mainstate.enter(nom, event)
        dir = 0
        nom.anim[0] = 1
        nom.anim[1] = 3
        frame = 0

    def exit(nom):
        mainstate.exit(nom)
        pass
    def do(nom):
        global frame
        nom.frame = frame//50
        frame += 1
        if nom.frame > 2:
            if nom.dir == 0: nom.add_event(CC.END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(CC.END_JUMP_MOVE)

        # MainState.do(nom)

    def draw(nom):
        mainstate.draw(nom)