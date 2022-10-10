from pico2d import *

Ongame = True
LEFT_KEY = False
RIGHT_KEY = False
JUMP = False


def key_events():
    global Ongame
    global LEFT_KEY
    global RIGHT_KEY
    global JUMP
    events = get_events()
    for event in events:
        # esc key
        if event.key == SDLK_ESCAPE:
            Ongame = False
        # left key
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            LEFT_KEY = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            LEFT_KEY = False
        # right key
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            RIGHT_KEY = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            RIGHT_KEY = False
        # jump key(space)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            JUMP = True
        elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
            JUMP = False
