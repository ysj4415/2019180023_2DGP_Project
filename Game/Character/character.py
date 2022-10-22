from Character.CharacterController.CharacterController import *
import window_size
import firering

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index
class Character:
    def __init__(self):
        self.x, self.y = window_size.width / 2, ground
        self.frame = 0
        self.image = load_image('res/character/PlayerCharacter.png')
        self.anim = [5, 7]
        self.speed = 0
        self.jumpradian = 0
        self.jumppower = 65
        self.rotation_radian = 0 / 360 * 2 * math.pi
        self.flip = ''
        self.floor_index = 0
        self.dir = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.frame_time = None

        self. life = 3

    def restart(self):
        self.x, self.y = window_size.width / 2, ground
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

    def add_event(self, event):
        self.event_que.insert(0,event)


    def jump(self):
        self.jumpradian = (self.jumpradian + 500 * self.frame_time//1) % 180
        f_index = (self.floor_index + 1) % 4
        jump_range = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index] + y_tuple[f_index])

        if jump_range == 0 :
            if self.dir == 0: self.add_event(END_JUMP_STOP)
            elif self.dir != 0: self.add_event(END_JUMP_MOVE)
            return True
        else: return False


    def wall_move(self, direction):
        f_index = (self.floor_index + 1) % 4


        if(direction == 'left'):
            self.rotation_radian -= 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index - 1) % 4

        if(direction == 'right'):
            self.rotation_radian += 90 / 360 * 2 * math.pi
            self.floor_index = (self.floor_index + 1) % 4

        jump = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index])
        self.x = (self.x + jump) * x_tuple[(self.floor_index) % 2]
        jump = jumprange(self.jumpradian, self.jumppower, y_tuple[f_index])
        self.y = (self.y + jump) * y_tuple[(self.floor_index) % 2]

        self.x = (self.x + (ground * x_tuple[(self.floor_index + 1) % 4])) % window_size.width
        self.y = (self.y + (ground * y_tuple[(self.floor_index + 1) % 4])) % window_size.height


    def move(self, dir):
        self.x += self.speed * x_tuple[self.floor_index] * dir
        self.y += self.speed * y_tuple[self.floor_index] * dir
        self.x = clamp(self.speed, self.x, window_size.width - self.speed)
        self.y = clamp(self.speed, self.y, window_size.height - self.speed)

    def empty_event_que(self):
        while len(self.event_que) > 0:
            event = self.event_que.pop()

    def update(self, frame_time):
        self.frame_time = frame_time
        self.speed = 300 * frame_time
        self.cur_state.do(self)

        y = self.y + jumprange(self.jumpradian, self.jumppower, 1)
        for range in firering.damagebox:
            print(range)
            print(self.x)
            print(y)


            if range[0][0] <= self.x <= range[1][0] and range[0][1] <= y - ground <= range[1][1]:
                self.life -= 1
                if self.life == 0:
                    self.restart()
                else:
                    self.add_event(DAMAGE)




        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)


            if event in next_state_table[self.cur_state]:
                self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)




    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event in next_state_table[self.cur_state]:
                self.add_event(key_event)
