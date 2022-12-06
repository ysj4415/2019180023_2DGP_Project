from Object.CharacterController.CharacterController import *
from Framework.Character import *
import window_size
from UI import Life
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm


RUN_SPEED_KMPH = 20.0
JUMP_SPEED_KMPH = 0.0

TIMER_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIMER_PER_ACTION

class nom(character):
    def __init__(self):
        super().__init__(window_size.width / 2, (ground + 10), IdleState)
        self.image_info = [0, 0, 64, 64]
        self.loadimage('res/character/PlayerCharacter.png')
        self.anim_type = 5
        self.frame_number = 7

        self.rotation_radian = 0 / 360 * 2 * math.pi

        self.SetKET(key_event_table)
        self.SetNST(next_state_table)
        # self. life = 3

        self.RUN_SPEED_KMPH = RUN_SPEED_KMPH
        self.JUMP_SPEED_KMPH = JUMP_SPEED_KMPH

        self.sound = load_wav('res/Windshield Hit With Bar.wav')
        self.sound.set_volume(25)

        self.c_left_x, self.c_bottom_y, self.c_right_x, self.c_top_y = 10,32,10,20
    def restart(self):
        self.position.translate.x, self.position.translate.y = window_size.width / 2, ground
        self.position.rotate = 0
        self.jumpradian = 0
        self.rotation_radian = 0 / 360 * 2 * math.pi
        self.floor_index = 0
        Life.life = 3

        self.speed = 0
        self.flip = ''
        self.anim = [5, 7]

        self.event_que = []
        if self.dir != 0: self.cur_state = RunState
        else: self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def wall_move(self, direction):
        map_size = game_framework.stack[-1].map_size

        if(direction == 'left'):
            self.position.rotate -= 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index - 1) % 4

        if(direction == 'right'):
            self.position.rotate += 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index + 1) % 4

        self.position.translate.x = self.position.translate.x * x_tuple[(self.floor_index) % 2]
        self.position.translate.y = self.position.translate.y * y_tuple[(self.floor_index) % 2]

        self.position.translate.x = (self.position.translate.x + (ground * x_tuple[(self.floor_index + 1) % 4])) % map_size[0]
        self.position.translate.y = (self.position.translate.y + (ground * y_tuple[(self.floor_index + 1) % 4])) % map_size[1]


    def update(self):
        super().update()
        # self.cur_state.do(self)


    def handle_collision(self, other, group):
        self.cur_state.handle_collision(self, other, group)
        if group == 'nom:up_floors':
            self.loadimage('res/character/PlayerCharacter_white.png')
        else:
            self.loadimage('res/character/PlayerCharacter.png')


    # def draw(self, x, y):
    #     super().draw( x, y)
    #     print('1')


