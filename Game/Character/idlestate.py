from Character import mainstate as ms

class IdleState:
    def enter(nom, event):

        ms.MainState.enter(nom, event)

        nom.anim[0] = 5
        nom.anim[1] = 7

    def exit(nom):
        ms.MainState.exit(nom)
        pass
    def do(nom):
        ms.MainState.do(nom)

    def draw(nom):
        ms.MainState.draw(nom)