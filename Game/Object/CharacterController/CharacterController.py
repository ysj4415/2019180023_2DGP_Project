from pico2d import *
from Object.CharacterController import jumpstate, attackstate, runstate, idlestate, hitstate

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,\
SPACE_DOWN, SPACE_UP, GOTO_IDLE, GOTO_MOVE,\
X_DOWN, X_UP, DAMAGE = range(11)


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
                RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, SPACE_UP: JumpState,
                 DAMAGE: HitState, GOTO_IDLE: IdleState, GOTO_MOVE: RunState},
    AttackState: {RIGHT_UP: AttackState, LEFT_UP: AttackState,
                RIGHT_DOWN: AttackState, LEFT_DOWN: AttackState,
                  GOTO_IDLE: IdleState, GOTO_MOVE: RunState},
    HitState:   {RIGHT_UP: HitState, LEFT_UP: HitState,
                RIGHT_DOWN: HitState, LEFT_DOWN: HitState,
                 GOTO_IDLE: IdleState, GOTO_MOVE: RunState,}
}