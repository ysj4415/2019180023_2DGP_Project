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


IdleState = idlestate.IdleState
RunState = runstate.RunState
JumpState = jumpstate.JumpState
AttackState = attackstate.AttackState
HitState = hitstate.HitState


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SPACE_DOWN: JumpState, X_DOWN: AttackState,
                DAMAGE: HitState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE_DOWN: JumpState, X_DOWN: AttackState,
                DAMAGE: HitState},
    JumpState: {  RIGHT_UP: JumpState, LEFT_UP: JumpState,
                RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState,
                 DAMAGE: HitState, END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState},
    AttackState: {RIGHT_UP: AttackState, LEFT_UP: AttackState,
                RIGHT_DOWN: AttackState, LEFT_DOWN: AttackState,
                  END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState},
    HitState:   {RIGHT_UP: HitState, LEFT_UP: HitState,
                RIGHT_DOWN: HitState, LEFT_DOWN: HitState,
                 END_JUMP_STOP: IdleState, END_JUMP_MOVE: RunState,}
}