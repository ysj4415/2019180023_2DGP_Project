from pico2d import *

import game_framework
import game_world
from Object.CharacterController.runstate import RunState

import server
import camera
from Object import Running_Nom
import button
title_image = None
nom = None


buttons = []
bgm = None

# 초기화
def enter():
    global buttons
    buttons = []
    global title_image
    global nom
    global s_button, e_button

    title_image = load_image('res/map/MainTitle.png')
    nom = Running_Nom.nom(300, 75)
    buttons.append(button.start_button(650, 200))
    buttons.append(button.end_button(650, 120))


    global bgm
    bgm = pico2d.load_music('res/Here it Comes - TrackTribe.mp3')

    bgm.set_volume(32)
    bgm.repeat_play()
    pass

# 종료
def exit_state():
    global bgm
    bgm.stop()

    for o in buttons:
        buttons.remove(o)
        del o
    pass
def update():
    nom.update()
    pass

# import window_size


def draw_world():
    title_image.draw(400,300)
    nom.draw()
    for button in buttons:
        button.draw()


def draw():
    pico2d.clear_canvas()
    draw_world()
    pico2d.update_canvas()


def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN:
        # esc key
            if event.key == pico2d.SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == pico2d.SDL_MOUSEMOTION:
            for button in buttons:
                if button.isInBox(event.x, 600 - event.y) == True:
                    button.size = 0.9
                else: button.size = 0.8

        if event.type == pico2d.SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                for button in buttons:
                    if button.isInBox(event.x, 600 - event.y) == True:
                        button.Click()


def pause():
    pass

def resume():
    pass



