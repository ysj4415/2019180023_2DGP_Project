from Object.CharacterController import mainstate


class RunState:

    def enter(nom, event):

        mainstate.MainState.enter(nom, event)
        nom.frame_count = 0
        nom.frame_speed = 40

        if nom.dir < 0:
            nom.flip = 'h'
        elif nom.dir > 0:
            nom.flip = ''

        nom.anim_type = 4
        nom.frame_number = 8


    def exit(nom):
        mainstate.MainState.exit(nom)
        pass

    def do(nom):
        mainstate.MainState.do(nom)

    def draw(nom):
        mainstate.MainState.draw(nom)