from Character.CharacterController import mainstate


class IdleState:
    def enter(nom, event):

        mainstate.MainState.enter(nom, event)

        nom.anim[0] = 5
        nom.anim[1] = 7

    def exit(nom):
        mainstate.MainState.exit(nom)
        pass
    def do(nom):
        mainstate.MainState.do(nom)

    def draw(nom):
        mainstate.MainState.draw(nom)