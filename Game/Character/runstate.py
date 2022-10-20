from Character import mainstate as ms

class RunState:

    def enter(nom, event):

        ms.MainState.enter(nom, event)

        if nom.dir < 0:
            nom.flip = 'h'
        elif nom.dir > 0:
            nom.flip = ''
        nom.anim[0] = 4
        nom.anim[1] = 8

    def exit(nom):
        ms.MainState.exit(nom)
        pass

    def do(nom):
        ms.MainState.do(nom)

    def draw(nom):
        ms.MainState.draw(nom)