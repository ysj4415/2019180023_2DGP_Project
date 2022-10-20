from pico2d import *
from Character import idlestate
from Character import jumpstate
from Character import runstate
from Character import hitstate
from Character import attackstate

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_DOWN, SPACE_UP, END_JUMP_STOP, END_JUMP_MOVE = range(8)
X_DOWN, X_UP = 8,9
DAMAGE = 10

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP,
    (SDL_KEYDOWN, SDLK_x): X_DOWN,
}

x_tuple = (1,0,-1,0)
y_tuple = (0,1,0,-1)

ground = 32

frame = None

# def jumprange(jumpradian, jumppower, index):
#     return jumppower * math.sin(jumpradian / 360 * 2 * math.pi) * index

# class MainState:
#     def enter(nom, event):
#         if event == RIGHT_DOWN:
#             nom.dir+=1
#         elif event == LEFT_DOWN:
#             nom.dir-=1
#         elif event ==  RIGHT_UP:
#             nom.dir-=1
#         elif event == LEFT_UP:
#             nom.dir+=1
#         nom.dir = clamp(-1, nom.dir, 1)
#         global frame
#         frame = 0
#     def exit(nom):
#         pass
#     def do(nom):
#         global frame
#         nom.frame = (frame // 50) % nom.anim[1]
#         nom.move(nom.dir)
#
#     def draw(nom):
#         f_index = (nom.floor_index + 1) % 4
#         nom.image.clip_composite_draw(nom.frame*64, nom.anim[0] * 64,
#                                         64, 64, nom.rotation_radian, nom.flip,
#                                        nom.x + jumprange(nom.jumpradian, nom.jumppower, x_tuple[f_index]),
#                                        nom.y + jumprange(nom.jumpradian, nom.jumppower, y_tuple[f_index]), 64, 64)
IdleState = idlestate.IdleState
# class IdleState:
#     def enter(nom, event):
#
#         MainState.enter(nom, event)
#
#         nom.anim[0] = 5
#         nom.anim[1] = 7
#
#     def exit(nom):
#         MainState.exit(nom)
#         pass
#     def do(nom):
#         global frame
#         MainState.do(nom)
#         frame += 1
#
#     def draw(nom):
#         MainState.draw(nom)

RunState = runstate.RunState
# class RunState:
#
#     def enter(nom, event):
#
#         MainState.enter(nom, event)
#
#         if nom.dir < 0:
#             nom.flip = 'h'
#         elif nom.dir > 0:
#             nom.flip = ''
#         nom.anim[0] = 4
#         nom.anim[1] = 8
#
#     def exit(nom):
#         MainState.exit(nom)
#         pass
#
#     def do(nom):
#         global frame
#         MainState.do(nom)
#         frame += 2
#
#     def draw(nom):
#         MainState.draw(nom)
JumpState = jumpstate.JumpState
# class JumpState:
#     def enter(nom, event):
#         MainState.enter(nom, event)
#
#         nom.anim[0] = 3
#         nom.anim[1] = 8
#
#     def exit(nom):
#         MainState.exit(nom)
#         nom.anim[0] = 5
#         nom.anim[1] = 7
#     def do(nom):
#         global frame
#         MainState.do(nom)
#         frame += 2
#
#         if nom.jump() == True: return 0
#
#         dir = ''
#         moveline = nom.x * x_tuple[nom.floor_index % 2] + nom.y * y_tuple[nom.floor_index % 2]
#         moveindex = x_tuple[nom.floor_index] + y_tuple[nom.floor_index]
#         move_winsize = window_size.width * x_tuple[nom.floor_index % 2] + window_size.height * y_tuple[nom.floor_index % 2]
#
#         if moveline == (0 + nom.speed * moveindex) % move_winsize:
#             dir = 'left'
#         elif moveline == (0 - nom.speed * moveindex) % move_winsize:
#             dir = 'right'
#
#         if(dir != '') :
#             nom.wall_move(dir)
#             nom.jumpradian = 0
#             nom.empty_event_que()
#             if nom.dir == 0: nom.add_event(END_JUMP_STOP)
#             elif nom.dir != 0: nom.add_event(END_JUMP_MOVE)
#     def draw(nom):
#         MainState.draw(nom)

AttackState = attackstate.AttackState
# class AttackState:
#     def enter(nom, event):
#         global frame
#         MainState.enter(nom, event)
#         dir = 0
#         nom.anim[0] = 1
#         nom.anim[1] = 3
#         frame = 0
#
#     def exit(nom):
#         MainState.exit(nom)
#         pass
#     def do(nom):
#         global frame
#         nom.frame = frame//50
#         frame += 1
#         if nom.frame > 2:
#             if nom.dir == 0: nom.add_event(END_JUMP_STOP)
#             elif nom.dir != 0: nom.add_event(END_JUMP_MOVE)
#
#         # MainState.do(nom)
#
#     def draw(nom):
#         MainState.draw(nom)
#
# dir = None
#
HitState = hitstate.HitState
# class HitState:
#     def enter(nom, event):
#         global frame
#         global dir
#         MainState.enter(nom, event)
#         dir = nom.dir
#         nom.anim[0] = 0
#         nom.anim[1] = 2
#         frame = 0
#         nom.jumpradian = 0
#         nom.y = 32
#     def exit(nom):
#         MainState.exit(nom)
#         pass
#     def do(nom):
#         global frame
#         nom.frame = (frame//20) % 2
#         frame += 1
#         if frame//20 > 2 * 6:
#             if nom.dir == 0: nom.add_event(END_JUMP_STOP)
#             elif nom.dir != 0: nom.add_event(END_JUMP_MOVE)
#         elif frame//20 < 3:
#             nom.move(dir * -1)
#         # MainState.do(nom)
#
#     def draw(nom):
#         MainState.draw(nom)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE_DOWN: JumpState, SPACE_UP: IdleState,
                X_DOWN: AttackState, X_UP: AttackState,
                DAMAGE: HitState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE_DOWN: JumpState, SPACE_UP: RunState,
                X_DOWN: AttackState, X_UP: AttackState,
                DAMAGE: HitState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState,
                LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState,
                SPACE_DOWN: JumpState, SPACE_UP: JumpState,
                X_DOWN: JumpState, DAMAGE: HitState,
                END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState},
    AttackState: {RIGHT_UP: AttackState, LEFT_UP: AttackState,
                LEFT_DOWN: AttackState, RIGHT_DOWN: AttackState,
                SPACE_DOWN: AttackState, SPACE_UP: AttackState,
                END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState, X_DOWN: AttackState},
    HitState:   {
                END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState,
                X_DOWN: HitState, DAMAGE: HitState}
}