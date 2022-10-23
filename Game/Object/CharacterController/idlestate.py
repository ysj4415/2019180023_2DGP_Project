from Object.CharacterController import mainstate


class IdleState:
    def enter(nom, event):

        mainstate.MainState.enter(nom, event)
        nom.frame_count = 0
        nom.frame_speed = 50
        nom.anim_type = 5
        nom.frame_number = 7


    def exit(nom):
        mainstate.MainState.exit(nom)
        pass
    def do(nom):
        mainstate.MainState.do(nom)

    def draw(nom):
        mainstate.MainState.draw(nom)