from Object.CharacterController import mainstate


class IdleState:
    @staticmethod
    def enter(nom, event):

        mainstate.MainState.enter(nom, event)
        nom.frame_count = 0
        nom.frame_speed = 50
        nom.anim_type = 5
        nom.frame_number = 7

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

    def handle_collision(nom, other, group):
        mainstate.MainState.handle_collision(nom, other, group)