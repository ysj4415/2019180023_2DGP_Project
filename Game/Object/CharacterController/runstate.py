from Object.CharacterController import mainstate


class RunState:
    @staticmethod
    def enter(nom, event):

        mainstate.MainState.enter(nom, event)

        if nom.dir < 0:
            nom.flip = 'h'
        elif nom.dir > 0:
            nom.flip = ''

        nom.anim_type = 4
        nom.frame_number = 8

    @staticmethod
    def exit(nom):
        mainstate.MainState.exit(nom)
        pass
    @staticmethod
    def do(nom):
        mainstate.MainState.do(nom)
    @staticmethod
    def draw(nom):
        mainstate.MainState.draw(nom)