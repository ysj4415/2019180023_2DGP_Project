from pico2d import *

import game_framework
import game_world
from Object.CharacterController.runstate import RunState

import server
import camera
from Object import Running_Nom
import button
title_image = None
import play_state

buttons = []
# 초기화
def enter():
    global buttons
    global title_image
    buttons = []

    title_image = load_image('res/UI/puase.png')
    buttons.append(button.continue_button(400, 350))
    buttons.append(button.title_button(400, 270))
    buttons.append(button.end_button(400, 190))

    pass

# 종료
def exit_state():
    # del title_image
    for o in buttons:
        buttons.remove(o)
        del o

    pass
def update():
    pass

# import window_size


def draw_world():
    title_image.draw(400,300)
    for button in buttons:
        button.draw()


def draw():
    pico2d.clear_canvas()
    play_state.draw_world()

    draw_world()
    pico2d.update_canvas()


def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN:
            # esc key
            if event.key == pico2d.SDLK_ESCAPE:
                game_framework.pop_state()
        elif event.type == pico2d.SDL_MOUSEMOTION:
            for button in buttons:
                if button.isInBox(event.x, 600 - event.y) == True:
                    button.size = 0.9
                else: button.size = 0.8

        if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for button in buttons:
                    if button.isInBox(event.x, 600 - event.y) == True:
                        print('ddd')
                        button.Click()


def pause():
    pass

def resume():
    pass



