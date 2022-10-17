import window_size
from Character.CharacterController import *
#
# RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP = range(6)
#
# key_event_table = {
#     (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
#     (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
#     (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
#     (SDL_KEYUP, SDLK_LEFT): LEFT_UP
# }
#
#
#
# x_tuple = (1,0,-1,0)
# y_tuple = (0,1,0,-1)
#
# ground = 32
#
# def jumprange(jumpradian, jumppower, index):
#     return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index
#
# class IdleState:
#     def enter(nom, event):
#         if event == RIGHT_DOWN:
#             nom.dir+=1
#         elif event == LEFT_DOWN:
#             nom.dir-=1
#         elif event ==  RIGHT_UP:
#             nom.dir-=1
#         elif event == LEFT_UP:
#             nom.dir+=1
#
#         if nom.dir == 0:
#             nom.anim[0] = 5
#             nom.anim[1] = 7
#         else:
#             if nom.dir < 0 : nom.flip = 'h'
#             elif nom.dir > 0 : nom.flip = ''
#             nom.anim[0] = 4
#             nom.anim[1] = 8
#         nom.timer = 1000
#     def exit(nom, event):
#         pass
#     def do(nom):
#         nom.frame = (nom.frame + 1) % nom.anim[1]
#
#     def draw(nom):
#         f_index = (nom.floor_index + 1) % 4
#
#         nom.image.clip_composite_draw(nom.frame*64, nom.anim[0] * 64,
#                                         64, 64, nom.rotation_radian, nom.flip,
#                                        nom.x + jumprange(nom.jumpradian, nom.jumppower, x_tuple[f_index]),
#                                        nom.y + jumprange(nom.jumpradian, nom.jumppower, y_tuple[f_index]), 64, 64)
# class RunState:
#     def enter(nom, event):
#         if event == RIGHT_DOWN:
#             nom.dir+=1
#             nom.flip = ''
#         elif event == LEFT_DOWN:
#             nom.dir-=1
#             nom.flip = 'h'
#         elif event ==  RIGHT_UP:
#             nom.dir-=1
#         elif event == LEFT_UP:
#             nom.dir+=1
#
#         if nom.dir == 0:
#             nom.anim[0] = 5
#             nom.anim[1] = 7
#         else:
#             if nom.dir < 0 : nom.flip = 'h'
#             elif nom.dir > 0 : nom.flip = ''
#             nom.anim[0] = 4
#             nom.anim[1] = 8
#     def exit(nom, event):
#         pass
#     def do(nom):
#         nom.frame = (nom.frame + 1) % nom.anim[1]
#         nom.move(nom.dir)
#
#     def draw(nom):
#         f_index = (nom.floor_index + 1) % 4
#         # self.image.clip_draw(self.frame*64, self.anim[0] * 64, 64, 64, self.x, self.y + jumprange(self.jumpradian, self.jumppower))
#         nom.image.clip_composite_draw(nom.frame*64, nom.anim[0] * 64,
#                                         64, 64, nom.rotation_radian, nom.flip,
#                                        nom.x + jumprange(nom.jumpradian, nom.jumppower, x_tuple[f_index]),
#                                        nom.y + jumprange(nom.jumpradian, nom.jumppower, y_tuple[f_index]), 64, 64)
#
#
# next_state_table = {
#     IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
#                 RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
#     RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
#                 LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState}
# }
class Charater:
    def __init__(self):
        self.x, self.y = window_size.width / 2, ground
        self.frame = 0
        self.image = load_image('PlayerCharacter.png')
        self.anim = [5, 7]
        self.speed = 7
        self.jumpradian = 0
        self.jumppower = 100
        self.rotation_radian = 0 / 360 * 2 * math.pi
        self.onair = False
        self.flip = ''
        self.floor_index = 0
        self.dir = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0,event)


    def jump(self):
        self.jumpradian = (self.jumpradian + 10) % 180

        f_index = (self.floor_index + 1) % 4
        jump_range = jumprange(self.jumpradian, self.jumppower, x_tuple[f_index] + y_tuple[f_index])

        if jump_range == 0 :
            self.cur_state.exit(self)
            self.cur_state = IdleState



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
        if self.speed <= self.x <= window_size.width - self.speed and self.speed <= self.y <= window_size.height - self.speed:
            self.x += self.speed * x_tuple[self.floor_index] * dir
            self.y += self.speed * y_tuple[self.floor_index] * dir
        if self.x < self.speed : self.x = self.speed
        elif self.x > window_size.width - self.speed: self.x = window_size.width - self.speed
        elif self.y < self.speed : self.y = self.speed
        elif self.y > window_size.height - self.speed: self.y = window_size.height - self.speed
    def update(self):
        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # if self.onair == True:
        #     self.anim[0] = 3
        #     self.anim[1] = 8
        #     self.jump()
        #
        #     dir = ''
        #     moveline = self.x * x_tuple[self.floor_index % 2] + self.y * y_tuple[self.floor_index % 2]
        #     moveindex = x_tuple[self.floor_index] + y_tuple[self.floor_index]
        #     move_winsize = window_size.width * x_tuple[self.floor_index % 2] + window_size.height * y_tuple[self.floor_index % 2]
        #
        #     if moveline == (0 + self.speed * moveindex) % move_winsize:
        #         dir = 'left'
        #     elif moveline == (0 - self.speed * moveindex) % move_winsize:
        #         dir = 'right'
        #
        #     if(dir != '') :
        #         self.wall_move(dir)
        #         self.onair = False
        #         self.jumpradian = 0

    def draw(self):
        self.cur_state.draw(self)
        delay(0.01)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
