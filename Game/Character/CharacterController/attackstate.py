from Character.CharacterController import mainstate
from Character.CharacterController import CharacterController as CC

frame = None

class AttackState:
    def enter(nom, event):
        mainstate.MainState.enter(nom, event)
        if event == CC.X_DOWN:
            global frame
            # mainstate.MainState.enter(nom, event)
            nom.anim[0] = 1
            nom.anim[1] = 3
            frame = 0

    def exit(nom):
        mainstate.MainState.exit(nom)
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
        mainstate.MainState.draw(nom)