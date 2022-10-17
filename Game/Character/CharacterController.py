from pico2d import *
import math
import window_size

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP, END_JUMP_STOP, END_JUMP_MOVE = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

x_tuple = (1,0,-1,0)
y_tuple = (0,1,0,-1)

ground = 32

def jumprange(jumpradian, jumppower, index):
    return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index

class MainState:
    def enter(nom, event):
        if event == RIGHT_DOWN:
            nom.dir+=1
        elif event == LEFT_DOWN:
            nom.dir-=1
        elif event ==  RIGHT_UP:
            nom.dir-=1
        elif event == LEFT_UP:
            nom.dir+=1
        nom.dir = clamp(-1, nom.dir, 1)
    def exit(nom):
        pass
    def do(nom):
        nom.frame = (nom.frame + 1) % nom.anim[1]
        nom.move(nom.dir)

    def draw(nom):
        f_index = (nom.floor_index + 1) % 4
        # self.image.clip_draw(self.frame*64, self.anim[0] * 64, 64, 64, self.x, self.y + jumprange(self.jumpradian, self.jumppower))
        nom.image.clip_composite_draw(nom.frame*64, nom.anim[0] * 64,
                                        64, 64, nom.rotation_radian, nom.flip,
                                       nom.x + jumprange(nom.jumpradian, nom.jumppower, x_tuple[f_index]),
                                       nom.y + jumprange(nom.jumpradian, nom.jumppower, y_tuple[f_index]), 64, 64)

class IdleState:
    def enter(nom, event):
        MainState.enter(nom, event)

        nom.anim[0] = 5
        nom.anim[1] = 7

    def exit(nom):
        MainState.exit(nom)
        pass
    def do(nom):
        print('dd')
        MainState.do(nom)

    def draw(nom):
        MainState.draw(nom)


class RunState:

    def enter(nom, event):
        MainState.enter(nom, event)
        if nom.dir < 0:
            nom.flip = 'h'
        elif nom.dir > 0:
            nom.flip = ''
        nom.anim[0] = 4
        nom.anim[1] = 8

    def exit(nom):
        MainState.exit(nom)
        pass

    def do(nom):
        MainState.do(nom)

    def draw(nom):
        MainState.draw(nom)

class JumpState:
    def enter(nom, event):
        MainState.enter(nom, event)

        nom.anim[0] = 3
        nom.anim[1] = 8

    def exit(nom):
        MainState.exit(nom)
        nom.anim[0] = 5
        nom.anim[1] = 7
    def do(nom):
        MainState.do(nom)
        if nom.jump() == True: return 0

        dir = ''
        moveline = nom.x * x_tuple[nom.floor_index % 2] + nom.y * y_tuple[nom.floor_index % 2]
        moveindex = x_tuple[nom.floor_index] + y_tuple[nom.floor_index]
        move_winsize = window_size.width * x_tuple[nom.floor_index % 2] + window_size.height * y_tuple[nom.floor_index % 2]

        if moveline == (0 + nom.speed * moveindex) % move_winsize:
            dir = 'left'
        elif moveline == (0 - nom.speed * moveindex) % move_winsize:
            dir = 'right'

        if(dir != '') :
            nom.wall_move(dir)
            nom.jumpradian = 0
            nom.empty_event_que()
            if nom.dir == 0: nom.add_event(END_JUMP_STOP)
            elif nom.dir != 0: nom.add_event(END_JUMP_MOVE)
    def draw(nom):
        MainState.draw(nom)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE_DOWN: JumpState, SPACE_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE_DOWN: JumpState, SPACE_UP: RunState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState,
                LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState,
                SPACE_DOWN: JumpState, SPACE_UP: JumpState,
                END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState}
}