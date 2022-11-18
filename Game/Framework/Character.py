from Framework.Pawn import *
# from Object.CharacterController.CharacterController import *
import window_size
import game_framework

PIXEL_PER_METER = (10.0/ 0.3)

class character(pawn):
    def __init__(self, x = 0, y = 0, state = None):
        super().__init__(x, y)

        self.dir = 0
        self.jumppower = 0

        self.event_que = []
        self.cur_state = state
        self.cur_state.enter(self, None)

        self.key_event_table = {}
        self.next_state_table = {}

        self.RUN_SPEED_KMPH = None
        self.JUMP_SPEED_KMPH = None

    def grabity(self):
        high = self.image_info[3] / 2

        self.JUMP_SPEED_KMPH -= 1.0



    def jump(self):
        high = self.image_info[3] / 2

        JUMP_SPEED_MPM = (self.JUMP_SPEED_KMPH * 1000.0 / 60.0)
        JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
        JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

        speed = JUMP_SPEED_PPS * game_framework.frame_time
        if self.floor_index == 0:
            self.position.translate.y += speed
            pass
        elif self.floor_index == 1:
            self.position.translate.x -= speed
            pass
        elif self.floor_index == 2:
            self.position.translate.y -= speed
            pass
        elif self.floor_index == 3:
            self.position.translate.x += speed
            pass


    def update(self):
        super().update()
        self.jump()

        self.grabity()

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            if event in self.next_state_table[self.cur_state]:
                self.cur_state = self.next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def move(self, dir):
        map_size = game_framework.stack[-1].map_size

        RUN_SPEED_MPM = (self.RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.position.translate.x +=  RUN_SPEED_PPS * game_framework.frame_time * self.x_tuple[self.floor_index] * dir
        self.position.translate.y += RUN_SPEED_PPS * game_framework.frame_time * self.y_tuple[self.floor_index] * dir
        self.position.translate.x = clamp(0, self.position.translate.x, map_size[0])
        self.position.translate.y = clamp(0, self.position.translate.y, map_size[1])


    def SetKET(self, key_event_table):
        self.key_event_table = key_event_table
    def SetNST(self, next_state_table):
        self.next_state_table = next_state_table


    def add_event(self, event):
        self.event_que.insert(0,event)
    def empty_event_que(self):
        while len(self.event_que) > 0:
            event = self.event_que.pop()
    def handle_event(self, event):
        if (event.type, event.key) in self.key_event_table:
            key_event = self.key_event_table[(event.type, event.key)]
            if key_event in self.next_state_table[self.cur_state]:
                self.add_event(key_event)


