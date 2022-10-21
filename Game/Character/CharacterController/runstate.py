from Character.CharacterController import mainstate


class RunState:

    def enter(nom, event):

        mainstate.MainState.enter(nom, event)

        if nom.dir < 0:
            nom.flip = 'h'
        elif nom.dir > 0:
            nom.flip = ''
        nom.anim[0] = 4
        nom.anim[1] = 8

    def exit(nom):
        mainstate.MainState.exit(nom)
        pass

    def do(nom):
        mainstate.MainState.do(nom)

    def draw(nom):
        mainstate.MainState.draw(nom)