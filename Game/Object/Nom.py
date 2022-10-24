from Object.CharacterController.CharacterController import *
from Framework.Character import *
import window_size
import firering
import spike

# def jumprange(jumpradian, jumppower, index):
#     return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index
class nom(character):
    def __init__(self):
        super().__init__(window_size.width / 2, ground, IdleState)
        self.image_info = [0, 0, 64, 64]
        self.loadimage('res/character/PlayerCharacter.png')
        self.anim_type = 5
        self.frame_number = 7

        self.speed = 0
        self.rotation_radian = 0 / 360 * 2 * math.pi

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.frame_time = None

        self. life = 3

    def restart(self):
        self.position.translate.x, self.position.translate.y = window_size.width / 2, ground
        self.jumpradian = 0
        self.rotation_radian = 0 / 360 * 2 * math.pi
        self.floor_index = 0
        self. life = 3

        self.speed = 0
        self.flip = ''
        self.anim = [5, 7]


        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)




    def wall_move(self, direction):
        f_index = (self.floor_index + 1) % 4


        if(direction == 'left'):
            self.position.rotate -= 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index - 1) % 4

        if(direction == 'right'):
            self.position.rotate += 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index + 1) % 4

        jump = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index])
        self.position.translate.x = (self.position.translate.x + jump) * x_tuple[(self.floor_index) % 2]
        jump = jumprange(self.jumpradian, self.jumppower, y_tuple[f_index])
        self.position.translate.y = (self.position.translate.y + jump) * y_tuple[(self.floor_index) % 2]

        self.position.translate.x = (self.position.translate.x + (ground * x_tuple[(self.floor_index + 1) % 4])) % window_size.width
        self.position.translate.y = (self.position.translate.y + (ground * y_tuple[(self.floor_index + 1) % 4])) % window_size.height



    def empty_event_que(self):
        while len(self.event_que) > 0:
            event = self.event_que.pop()

    def update(self, frame_time):
        self.frame_time = frame_time
        self.speed = 300 * frame_time

        self.cur_state.do(self)

        damagebox = firering.damagebox + spike.damagebox
        y = self.position.translate.y + jumprange(self.jumpradian, self.jumppower, 1)
        for range in damagebox:
            if range[0][0] <= self.position.translate.x <= range[1][0] and range[0][1] <= y - ground <= range[1][1]:
                if self.cur_state != HitState: self.add_event(DAMAGE)


        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            if event in next_state_table[self.cur_state]:
                self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def add_event(self, event):
        self.event_que.insert(0,event)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event in next_state_table[self.cur_state]:
                self.add_event(key_event)
    def draw(self):
        self.cur_state.draw(self)

